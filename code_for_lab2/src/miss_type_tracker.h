#ifndef MISS_TYPE_TRACKER_H
#define MISS_TYPE_TRACKER_H

#include <cstdint>

#ifdef __cplusplus
extern "C" {
#endif

// Initialize the miss tracker
void init_miss_tracker();

// Classify a miss as compulsory, capacity, or conflict
void classify_miss(uint64_t block_addr, bool was_evicted);

// Get the count of compulsory misses
int get_compulsory_miss_count();

// Get the count of capacity misses
int get_capacity_miss_count();

// Get the count of conflict misses
int get_conflict_miss_count();

#ifdef __cplusplus
}
#endif

#endif // MISS_TYPE_TRACKER_H
