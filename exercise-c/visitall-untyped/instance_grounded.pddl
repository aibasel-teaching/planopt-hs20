(define (problem instance-grounded)
(:domain grid-visit-all-grounded-for-instance)
(:objects
)
(:init
   (at-robot-loc-x0-y0)
   (visited-loc-x0-y0)
)
(:goal
    (and
        (visited-loc-x0-y0)
        (visited-loc-x1-y0)
        (visited-loc-x1-y1)
        (visited-loc-x2-y0)
    )
)
)
