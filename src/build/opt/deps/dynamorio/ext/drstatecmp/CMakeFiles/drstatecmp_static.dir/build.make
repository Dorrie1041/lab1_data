# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dongruishen/scarab/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dongruishen/scarab/src/build/opt

# Include any dependencies generated for this target.
include deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/depend.make

# Include the progress variables for this target.
include deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/progress.make

# Include the compile flags for this target's objects.
include deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/flags.make

deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/drstatecmp.c.o: deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/flags.make
deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/drstatecmp.c.o: ../../deps/dynamorio/ext/drstatecmp/drstatecmp.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/dongruishen/scarab/src/build/opt/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/drstatecmp.c.o"
	cd /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -m64 -fno-strict-aliasing -funsigned-char -fno-stack-protector -fvisibility=internal -std=gnu99 -fno-unwind-tables -O3 -g3 -Wall -Werror -Wwrite-strings -Wvla -Wno-unused-but-set-variable -Wno-stringop-truncation -Wno-format-truncation -Wno-stringop-overflow -fno-stack-protector -nostdlib -m64 -o CMakeFiles/drstatecmp_static.dir/drstatecmp.c.o   -c /home/dongruishen/scarab/src/deps/dynamorio/ext/drstatecmp/drstatecmp.c

deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/drstatecmp.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/drstatecmp_static.dir/drstatecmp.c.i"
	cd /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -m64 -fno-strict-aliasing -funsigned-char -fno-stack-protector -fvisibility=internal -std=gnu99 -fno-unwind-tables -O3 -g3 -Wall -Werror -Wwrite-strings -Wvla -Wno-unused-but-set-variable -Wno-stringop-truncation -Wno-format-truncation -Wno-stringop-overflow -fno-stack-protector -nostdlib -m64 -E /home/dongruishen/scarab/src/deps/dynamorio/ext/drstatecmp/drstatecmp.c > CMakeFiles/drstatecmp_static.dir/drstatecmp.c.i

deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/drstatecmp.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/drstatecmp_static.dir/drstatecmp.c.s"
	cd /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -m64 -fno-strict-aliasing -funsigned-char -fno-stack-protector -fvisibility=internal -std=gnu99 -fno-unwind-tables -O3 -g3 -Wall -Werror -Wwrite-strings -Wvla -Wno-unused-but-set-variable -Wno-stringop-truncation -Wno-format-truncation -Wno-stringop-overflow -fno-stack-protector -nostdlib -m64 -S /home/dongruishen/scarab/src/deps/dynamorio/ext/drstatecmp/drstatecmp.c -o CMakeFiles/drstatecmp_static.dir/drstatecmp.c.s

# Object files for target drstatecmp_static
drstatecmp_static_OBJECTS = \
"CMakeFiles/drstatecmp_static.dir/drstatecmp.c.o"

# External object files for target drstatecmp_static
drstatecmp_static_EXTERNAL_OBJECTS =

deps/dynamorio/ext/lib64/release/libdrstatecmp_static.a: deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/drstatecmp.c.o
deps/dynamorio/ext/lib64/release/libdrstatecmp_static.a: deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/build.make
deps/dynamorio/ext/lib64/release/libdrstatecmp_static.a: deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/dongruishen/scarab/src/build/opt/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library ../lib64/release/libdrstatecmp_static.a"
	cd /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp && $(CMAKE_COMMAND) -P CMakeFiles/drstatecmp_static.dir/cmake_clean_target.cmake
	cd /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/drstatecmp_static.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/build: deps/dynamorio/ext/lib64/release/libdrstatecmp_static.a

.PHONY : deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/build

deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/clean:
	cd /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp && $(CMAKE_COMMAND) -P CMakeFiles/drstatecmp_static.dir/cmake_clean.cmake
.PHONY : deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/clean

deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/depend:
	cd /home/dongruishen/scarab/src/build/opt && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dongruishen/scarab/src /home/dongruishen/scarab/src/deps/dynamorio/ext/drstatecmp /home/dongruishen/scarab/src/build/opt /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp /home/dongruishen/scarab/src/build/opt/deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : deps/dynamorio/ext/drstatecmp/CMakeFiles/drstatecmp_static.dir/depend
