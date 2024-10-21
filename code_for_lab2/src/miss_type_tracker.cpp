#include "miss_type_tracker.h"
#include <unordered_map>
#include <cstdint>

enum MissType {
    COMPULSORY,
    CAPACITY,
    CONFLICT
};

struct BlockState {
    bool accessed;
    bool was_evicted;
};

// Map to track block addresses and their state
static std::unordered_map<uint64_t, BlockState> block_states;
static int compulsory_miss_count = 0;
static int capacity_miss_count = 0;
static int conflict_miss_count = 0;

extern "C" {

// Initialize the miss tracker
void init_miss_tracker() {
    block_states.clear();
    compulsory_miss_count = 0;
    capacity_miss_count = 0;
    conflict_miss_count = 0;
}

// Classify a miss and update the appropriate miss count
void classify_miss(uint64_t block_addr, bool was_evicted) {
    BlockState &state = block_states[block_addr];

    if (!state.accessed) {
        // Compulsory miss (first access to this block)
        compulsory_miss_count++;
        state.accessed = true;
    } else if (was_evicted) {
        if (state.was_evicted) {
            // Capacity miss (block was evicted and brought back)
            capacity_miss_count++;
        } else {
            // Conflict miss (block was in cache but replaced due to conflict)
            conflict_miss_count++;
        }
    }
    // Update the eviction state
    state.was_evicted = was_evicted;
}

// Getters for the miss counts
int get_compulsory_miss_count() {
    return compulsory_miss_count;
}

int get_capacity_miss_count() {
    return capacity_miss_count;
}

int get_conflict_miss_count() {
    return conflict_miss_count;
}

}
