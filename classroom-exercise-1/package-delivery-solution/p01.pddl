(define (problem mydomain-example)

  (:domain mydomain)

  (:objects
    c1 c2 c3 t1 p1 p2
  )

  (:init
    (IS-CITY c1)
    (IS-CITY c2)
    (IS-CITY c3)
    (IS-TRUCK t1)
    (IS-PACKAGE p1)
    (IS-PACKAGE p2)
    (CONNECTED c1 c2)
    (CONNECTED c1 c3)
    (CONNECTED c2 c1)
    (CONNECTED c2 c3)
    (CONNECTED c3 c1)
    (CONNECTED c3 c2)
    (truck-at t1 c1)
    (package-at p1 c2)
    (package-at p2 c3)
  )

  (:goal (and (package-at p1 c3) (package-at p2 c2)))
)