(define (domain grid-visit-all-grounded-for-instance)
    (:requirements )
    (:predicates
        (at-robot-loc-x0-y0)
        (at-robot-loc-x1-y0)
        (at-robot-loc-x1-y1)
        (at-robot-loc-x2-y0)
        (visited-loc-x0-y0)
        (visited-loc-x1-y0)
        (visited-loc-x1-y1)
        (visited-loc-x2-y0)
    )
    (:action move-loc-x0-y0-loc-x1-y0
        :parameters ()
        :precondition 
        (at-robot-loc-x0-y0)
        :effect 
        (and
            (at-robot-loc-x1-y0)
            (not (at-robot-loc-x0-y0))
            (visited-loc-x1-y0)
        )
    )
    (:action move-loc-x1-y0-loc-x0-y0
        :parameters ()
        :precondition 
        (at-robot-loc-x1-y0)
        :effect 
        (and
            (at-robot-loc-x0-y0)
            (not (at-robot-loc-x1-y0))
            (visited-loc-x0-y0)
        )
    )
    (:action move-loc-x1-y0-loc-x1-y1
        :parameters ()
        :precondition 
        (at-robot-loc-x1-y0)
        :effect 
        (and
            (at-robot-loc-x1-y1)
            (not (at-robot-loc-x1-y0))
            (visited-loc-x1-y1)
        )
    )
    (:action move-loc-x1-y1-loc-x1-y0
        :parameters ()
        :precondition 
        (at-robot-loc-x1-y1)
        :effect 
        (and
            (at-robot-loc-x1-y0)
            (not (at-robot-loc-x1-y1))
            (visited-loc-x1-y0)
        )
    )
    (:action move-loc-x1-y0-loc-x2-y0
        :parameters ()
        :precondition 
        (at-robot-loc-x1-y0)
        :effect 
        (and
            (at-robot-loc-x2-y0)
            (not (at-robot-loc-x1-y0))
            (visited-loc-x2-y0)
        )
    )
    (:action move-loc-x2-y0-loc-x1-y0
        :parameters ()
        :precondition 
        (at-robot-loc-x2-y0)
        :effect 
        (and
            (at-robot-loc-x1-y0)
            (not (at-robot-loc-x2-y0))
            (visited-loc-x1-y0)
        )
    )
)
