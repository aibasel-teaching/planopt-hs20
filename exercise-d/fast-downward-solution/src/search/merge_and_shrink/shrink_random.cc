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

    // Fill a vector with all states and shuffle it to have a random order.
    vector<int> states(num_states);
    iota(states.begin(), states.end(), 0);
    local_rng.shuffle(states);

    /*
      Go over all states and, as long size allows, create one equivalence
      class for each state, and once the size limit is reached, randomly
      assign states to existing equivalence classes.
    */
    equivalence_relation.reserve(min(num_states, target_size));
    for (int state : states) {
        if (static_cast<int>(equivalence_relation.size()) < target_size) {
            equivalence_relation.push_back(forward_list<int>());
            equivalence_relation.back().push_front(state);
        } else {
            assert(static_cast<int>(equivalence_relation.size()) == target_size);
            int random_number = local_rng(target_size);
            assert(!equivalence_relation[random_number].empty());
            equivalence_relation[random_number].push_front(state);
        }
    }
    assert(static_cast<int>(equivalence_relation.size()) == min(num_states, target_size));

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
