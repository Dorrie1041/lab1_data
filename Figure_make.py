import os
import json
import argparse
import matplotlib.pyplot as plt
import numpy as np
import csv

# Helper function to read descriptor data from JSON
def read_descriptor_from_json(descriptor_filename):
    try:
        with open(descriptor_filename, 'r') as json_file:
            descriptor_data = json.load(json_file)
        return descriptor_data
    except FileNotFoundError:
        print(f"Error: File '{descriptor_filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{descriptor_filename}': {e}")
        return None

# Helper function to extract specific stats from the CSV files
def get_stats_from_csv(file_path, stat_name):
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if stat_name in row[0]:
                    return int(row[1].strip())
    except Exception as e:
        print(f"Error reading {stat_name} from {file_path}: {e}")
    return 0

# Function to compute branch misprediction ratio and generate plot
def get_branch_misprediction_ratio(descriptor_data, sim_path, output_dir):
    benchmarks_org = descriptor_data["workloads_list"].copy()
    benchmarks = []
    branch_mispred_ratio = {}

    try:
        for config_key in descriptor_data["configurations"].keys():
            ratio_config = []
            avg_ratio_config = 0.0
            cnt_benchmarks = 0
            for benchmark in benchmarks_org:
                benchmark_name = benchmark.split("/")
                exp_path = sim_path + '/' + benchmark + '/' + descriptor_data["experiment"] + '/'

                mispredictions = 0
                executed_branches = 0

                # Read from power.stat.0.csv for branch mispredictions and executed branches
                with open(exp_path + config_key + '/power.stat.0.csv') as f:
                    lines = f.readlines()
                    for line in lines:
                        if 'POWER_BRANCH_MISPREDICT_count' in line:
                            tokens = [x.strip() for x in line.split(',')]
                            mispredictions = int(tokens[1])
                        if 'POWER_BRANCH_OP_count' in line:
                            tokens = [x.strip() for x in line.split(',')]
                            executed_branches = int(tokens[1])

                # Calculate branch misprediction ratio
                ratio = mispredictions / executed_branches if executed_branches > 0 else 0
                avg_ratio_config += ratio

                cnt_benchmarks += 1
                if len(benchmarks_org) > len(benchmarks):
                    benchmarks.append(benchmark_name)

                ratio_config.append(ratio)

            # Append average ratio for this configuration
            num = len(benchmarks)
            ratio_config.append(avg_ratio_config / num)
            branch_mispred_ratio[config_key] = ratio_config

        # Add 'Avg' to the benchmark list
        benchmarks.append('Avg')

        # Plot the Branch Misprediction Ratio data
        plot_data(benchmarks, branch_mispred_ratio, 'Branch Misprediction Ratio', output_dir + '/Branch_Misprediction_Ratio.png')

    except Exception as e:
        print(e)

def get_dcache_miss_ratio(descriptor_data, sim_path, output_dir):
    benchmarks_org = descriptor_data["workloads_list"].copy()
    benchmarks = []
    dcache_miss_ratio = {}

    try:
        for config_key in descriptor_data["configurations"].keys():
            ratio_config = []
            avg_ratio_config = 0.0
            cnt_benchmarks = 0
            for benchmark in benchmarks_org:
                benchmark_name = benchmark.split("/")[-1]
                exp_path = sim_path + '/' + benchmark + '/' + descriptor_data["experiment"] + '/'

                dcache_misses = 0
                dcache_hits = 0

                # Read from memory.stat.0.csv for DCache misses and hits
                with open(exp_path + config_key + '/memory.stat.0.csv') as f:
                    for line in f:
                        if "DCACHE_HIT_count" in line and "DC_PREF_REQ_DCACHE_HIT_count" not in line:
                            print("HIT line: ", line.strip())  # Debug print
                            dcache_hits = int(line.split(',')[1].strip())
                        elif "DCACHE_MISS_count" in line and "NUM_WINDOWS_WITH_DCACHE_MISS_count" not in line:
                            print("MISS line: ", line.strip())  # Debug print
                            dcache_misses = int(line.split(',')[1].strip())

                # Debugging print for the current benchmark
                print(f"Benchmark: {benchmark_name}, DCache Misses: {dcache_misses}, DCache Hits: {dcache_hits}")

                # Calculate DCache miss ratio
                dcache_accesses = dcache_misses + dcache_hits
                if dcache_accesses > 0:
                    ratio = dcache_misses / dcache_accesses
                else:
                    ratio = 0

                avg_ratio_config += ratio
                cnt_benchmarks += 1

                # Append benchmark name if not already done
                if len(benchmarks_org) > len(benchmarks):
                    benchmarks.append(benchmark_name)

                ratio_config.append(ratio)

            # Append average ratio for this configuration
            if cnt_benchmarks > 0:
                ratio_config.append(avg_ratio_config / cnt_benchmarks)
            else:
                ratio_config.append(0)
            dcache_miss_ratio[config_key] = ratio_config

        # Add 'Avg' to the benchmark list
        benchmarks.append('Avg')

        # Plot the DCache Miss Ratio data
        plot_data(benchmarks, dcache_miss_ratio, 'DCache Miss Ratio', output_dir + '/DCache_Miss_Ratio.png')

    except Exception as e:
        print(e)

def get_icache_miss_ratio(descriptor_data, sim_path, output_dir):
    benchmarks_org = descriptor_data["workloads_list"].copy()
    benchmarks = []
    icache_miss_ratio = {}

    try:
        for config_key in descriptor_data["configurations"].keys():
            ratio_config = []
            avg_ratio_config = 0.0
            cnt_benchmarks = 0
            for benchmark in benchmarks_org:
                benchmark_name = benchmark.split("/")
                exp_path = sim_path + '/' + benchmark + '/' + descriptor_data["experiment"] + '/'
                
                icache_misses = 0
                icache_hits = 0
                
                # Read from memory.stat.0.csv for ICache misses and hits
                with open(exp_path + config_key + '/memory.stat.0.csv') as f:
                    lines = f.readlines()
                    for line in lines:
                        if 'ICACHE_MISS_count' in line:
                            tokens = [x.strip() for x in line.split(',')]
                            icache_misses = int(tokens[1])
                        if 'ICACHE_HIT_count' in line:
                            tokens = [x.strip() for x in line.split(',')]
                            icache_hits = int(tokens[1])

                # Calculate ICache miss ratio
                icache_accesses = icache_misses + icache_hits
                ratio = icache_misses / icache_accesses if icache_accesses > 0 else 0
                avg_ratio_config += ratio

                cnt_benchmarks += 1
                if len(benchmarks_org) > len(benchmarks):
                    benchmarks.append(benchmark_name)

                ratio_config.append(ratio)

            # Append average ratio for this configuration
            num = len(benchmarks)
            ratio_config.append(avg_ratio_config / num)
            icache_miss_ratio[config_key] = ratio_config

        # Add 'Avg' to the benchmark list
        benchmarks.append('Avg')

        # Plot the ICache Miss Ratio data
        plot_data(benchmarks, icache_miss_ratio, 'ICache Miss Ratio', output_dir + '/ICache_Miss_Ratio.png')

    except Exception as e:
        print(e)
def get_IPC(descriptor_data, sim_path, output_dir):
  benchmarks_org = descriptor_data["workloads_list"].copy()
  benchmarks = []
  ipc = {}

  try:
    for config_key in descriptor_data["configurations"].keys():
      ipc_config = []
      avg_IPC_config = 0.0
      cnt_benchmarks = 0
      for benchmark in benchmarks_org:
        benchmark_name = benchmark.split("/")
        exp_path = sim_path+'/'+benchmark+'/'+descriptor_data["experiment"]+'/'
        IPC = 0
        with open(exp_path+config_key+'/memory.stat.0.csv') as f:
          lines = f.readlines()
          for line in lines:
            if 'Periodic IPC' in line:
              tokens = [x.strip() for x in line.split(',')]
              IPC = float(tokens[1])
              break

        avg_IPC_config += IPC

        cnt_benchmarks = cnt_benchmarks + 1
        if len(benchmarks_org) > len(benchmarks):
          benchmarks.append(benchmark_name)

        ipc_config.append(IPC)

      num = len(benchmarks)
      print(benchmarks)
      ipc_config.append(avg_IPC_config/num)
      ipc[config_key] = ipc_config

    benchmarks.append('Avg')
    plot_data(benchmarks, ipc, 'IPC', output_dir+'/IPC.png')

  except Exception as e:
    print(e)        

def plot_data(benchmarks, data, ylabel_name, fig_name, ylim=None):
    import numpy as np
    import matplotlib.pyplot as plt

    colors = ['#800000', '#911eb4', '#4363d8', '#f58231', '#3cb44b', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#e6beff', '#e6194b', '#000075', '#800000', '#9a6324', '#808080', '#ffffff', '#000000']
    ind = np.arange(len(benchmarks)) * 2  # Increase space between applications
    width = 0.25  # Slightly wider bars for less overlap
    fig, ax = plt.subplots(figsize=(16, 8), dpi=80)
    num_keys = len(data.keys())

    idx = 0
    start_id = -int(num_keys / 1.5)  # Adjust this for better spacing between bars within an application
    for key in data.keys():
        hatch = ''
        if idx % 2:
            hatch = '\\\\'
        else:
            hatch = '///'
        ax.bar(ind + (start_id + idx) * width, data[key], width=width, fill=False, hatch=hatch, color=colors[idx], edgecolor=colors[idx], label=key)
        idx += 1

    ax.set_xlabel("Benchmarks")
    ax.set_ylabel(ylabel_name)
    
    # Adjust x-tick positions
    ax.set_xticks(ind)
    
    # Rotate the labels
    ax.set_xticklabels(benchmarks, rotation=45, ha='right', fontsize=10)
    
    ax.grid('x')

    if ylim is not None:
        ax.set_ylim(ylim)
    
    ax.legend(loc="upper left", ncols=2)
    fig.tight_layout()

    # Save the figure
    plt.savefig(fig_name, format="png", bbox_inches="tight")
    plt.close()

# Main function to parse arguments and call the branch misprediction function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Branch Misprediction Ratio plot')
    parser.add_argument('-o', '--output_dir', required=True, help='Output directory. Usage: -o /path/to/output')
    parser.add_argument('-d', '--descriptor_name', required=True, help='Descriptor JSON file. Usage: -d /path/to/lab1.json')
    parser.add_argument('-s', '--simulation_path', required=True, help='Simulation results directory. Usage: -s /path/to/simulations')

    args = parser.parse_args()

    descriptor_filename = args.descriptor_name
    descriptor_data = read_descriptor_from_json(descriptor_filename)

    if descriptor_data:
        get_IPC(descriptor_data, args.simulation_path, args.output_dir)  