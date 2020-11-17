#include "shrink_random.h"

#include "transition_system.h"

#include "../option_parser.h"
#include "../plugin.h"

#include "../utils/rng.h"
#include "../utils/rng_options.h"

#include <algorithm>
#include <cassert>
#include <numeric>
#include <random>

using namespace std;

namespace merge_and_shrink {
ShrinkRandom::ShrinkRandom(const Options &opts)
    : ShrinkStrategy(),
      rng(utils::parse_rng_from_options(opts)) {
}

StateEquivalenceRelation ShrinkRandom::compute_equivalence_relation(
    const TransitionSystem &ts,
    const Distances &,
    int target_size) const {
    int num_states = ts.get_size();
    StateEquivalenceRelation equivalence_relation;
    utils::RandomNumberGenerator &local_rng = *rng;

    /*
      TODO: add your code for exercise 5(b) here.

      States of the given transition system are represented as integers from 0
      to n-1 if n is the size of the transition system; thus you only need to
      know how many states there are (already stored in num_states). Compute a
      partioning of the states as described in the exercise. The result should
      be stored in equivalence_relation, which is a vector<forward_list<int>>.
      Each entry forward_list<int> of the vector is one class of states that
      will be abstracted to the same, new abstract state. You can use
      push_front on forward_list to insert states.

      You can use local_rng(x) for some int x to generate a random
      number in [0..x). See src/search/utils/rng.h for other methods of random
      number generators. Of course, you can also use standard library solutions.
    */

    return equivalence_relation;
}

string ShrinkRandom::name() const {
    return "random";
}

void ShrinkRandom::dump_strategy_specific_options() const {
}

static shared_ptr<ShrinkStrategy>_parse(OptionParser &parser) {
    utils::add_rng_options(parser);

    Options opts = parser.parse();

    if (parser.help_mode())
        return nullptr;

    if (parser.dry_run())
        return nullptr;
    else
        return make_shared<ShrinkRandom>(opts);
}

static Plugin<ShrinkStrategy> _plugin("shrink_random", _parse);
}
