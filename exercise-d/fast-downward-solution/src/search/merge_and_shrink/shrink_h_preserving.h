#ifndef MERGE_AND_SHRINK_SHRINK_H_PRESERVING_H
#define MERGE_AND_SHRINK_SHRINK_H_PRESERVING_H

#include "shrink_strategy.h"

namespace merge_and_shrink {
class ShrinkHPreserving : public ShrinkStrategy {
protected:
    virtual void dump_strategy_specific_options() const override;
    virtual std::string name() const override;
public:
    ShrinkHPreserving();
    virtual ~ShrinkHPreserving() override = default;
    virtual StateEquivalenceRelation compute_equivalence_relation(
        const TransitionSystem &ts,
        const Distances &distances,
        int target_size) const override;

    virtual bool requires_init_distances() const override {
        return false;
    }

    virtual bool requires_goal_distances() const override {
        return true;
    }
};
}

#endif
