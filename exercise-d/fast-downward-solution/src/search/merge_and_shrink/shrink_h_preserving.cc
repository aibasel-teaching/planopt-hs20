#include "shrink_h_preserving.h"

#include "distances.h"
#include "transition_system.h"

#include "../option_parser.h"
#include "../plugin.h"

#include <algorithm>
#include <cassert>
#include <map>

using namespace std;

namespace merge_and_shrink {
ShrinkHPreserving::ShrinkHPreserving() : ShrinkStrategy() {
}

StateEquivalenceRelation ShrinkHPreserving::compute_equivalence_relation(
    const TransitionSystem &ts,
    const Distances &distances,
    int target_size) const {
    assert(distances.are_goal_distances_computed());
    int num_states = ts.get_size();
    StateEquivalenceRelation equivalence_relation;

    // Partition states according to their h-value.
    map<int, StateEquivalenceClass> h_to_states;
    for (int state = 0; state < num_states; ++state) {
        int h = distances.get_goal_distance(state);
        h_to_states[h].push_front(state);
    }

    /*
      Go over each partition in increasing order of their h-value and as long
      as size allows, make the partition its own equivalence class. If the
      size limit is reached, put all remaining states from all remaining
      partitions into the last equivalence class.
    */
    equivalence_relation.reserve(min(target_size, static_cast<int>(h_to_states.size())));
    for (auto it : h_to_states) {
        if (static_cast<int>(equivalence_relation.size()) == target_size) {
            // The equivalence relation is already full, so we add all
            // remaining states into the equivalence class that was added last.
            for (int state : it.second) {
                equivalence_relation.back().push_front(state);
            }
        } else {
            // The equivalence relation can still grow, so we put all states
            // of the current h-value into their own equivalence class.
            equivalence_relation.push_back(move(it.second));
        }
    }
    assert(static_cast<int>(equivalence_relation.size())
        == min(target_size, static_cast<int>(h_to_states.size())));

    return equivalence_relation;
}

string ShrinkHPreserving::name() const {
    return "h-preserving";
}

void ShrinkHPreserving::dump_strategy_specific_options() const {
}

static shared_ptr<ShrinkStrategy>_parse(OptionParser &parser) {
    if (parser.help_mode())
        return nullptr;

    if (parser.dry_run())
        return nullptr;
    else
        return make_shared<ShrinkHPreserving>();
}

static Plugin<ShrinkStrategy> _plugin("shrink_h_preserving", _parse);
}
