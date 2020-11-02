#include "shrink_h_preserving.h"

#include "distances.h"
#include "transition_system.h"

#include "../option_parser.h"
#include "../plugin.h"

#include <algorithm>
#include <cassert>

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

    /*
      TODO: add your code for exercise 5(a) here.

      States of the given transition system are represented as integers from 0
      to n-1 if n is the size of the transition system; thus you only need to
      know how many states there are (already stored in num_states). Compute a
      partioning of the states as described in the exercise. The result should
      be stored in equivalence_relation, which is a vector<forward_list<int>>.
      Each entry forward_list<int> of the vector is one class of states that
      will be abstracted to the same, new abstract state. You can use
      push_front on forward_list to insert states.
    */

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
