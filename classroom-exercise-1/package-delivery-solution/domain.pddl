(define (domain mydomain)
  (:requirements :strips)
  
  (:predicates
    (IS-CITY ?c)  
    (IS-TRUCK ?t)
    (IS-PACKAGE ?p)
    (truck-at ?t ?c)
    (package-at ?p ?c)
    (package-in ?p ?t)
    (CONNECTED ?c1 ?c2)
  )
  
  (:action move
    :parameters (?t ?c1 ?c2)
    :precondition (and 
                    (IS-TRUCK ?t)
                    (IS-CITY ?c1)
                    (IS-CITY ?c2)
                    (truck-at ?t ?c1)
                    (CONNECTED ?c1 ?c2)
                  )
    :effect (and (not (truck-at ?t ?c1))
                 (truck-at ?t ?c2)
            )
  )
  
  (:action load
    :parameters (?t ?p ?c)
    :precondition (and 
                    (IS-TRUCK ?t)
                    (IS-PACKAGE ?p)
                    (IS-CITY ?c)
                    (truck-at ?t ?c)
                    (package-at ?p ?c)
                  )
    :effect (and (not (package-at ?p ?c))
                 (package-in ?p ?t)
            )
    )

  (:action unload
    :parameters (?t ?p ?c)
    :precondition (and 
                    (IS-TRUCK ?t)
                    (IS-PACKAGE ?p)
                    (IS-CITY ?c)
                    (truck-at ?t ?c)
                    (package-in ?p ?t)
                  )
    :effect (and (not (package-in ?p ?t))
                 (package-at ?p ?c)
            )
    )
)