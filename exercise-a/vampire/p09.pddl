(define (problem p09)
(:domain vampire)
;
; Room1 Room2 Room3 Room4 Room5 Room6 Room7 Room8 Room9 Room10 Room11 Room12 Room13 Room14 Room15
; 1S    0     0     1     0     0     0G    0V    0     0      0      0      0      0      0
;
(:objects
    room1
    room2
    room3
    room4
    room5
    room6
    room7
    room8
    room9
    room10
    room11
    room12
    room13
    room14
    room15
)
(:init
    (slayer-is-alive)
    (slayer-is-in room1)

    (vampire-is-alive)
    (vampire-is-in room8)

    (light-on room1)
    (light-on room4)

    (CONTAINS-GARLIC room7)

    (NEXT-ROOM room1 room2)
    (NEXT-ROOM room2 room3)
    (NEXT-ROOM room3 room4)
    (NEXT-ROOM room4 room5)
    (NEXT-ROOM room5 room6)
    (NEXT-ROOM room6 room7)
    (NEXT-ROOM room7 room8)
    (NEXT-ROOM room8 room9)
    (NEXT-ROOM room9 room10)
    (NEXT-ROOM room10 room11)
    (NEXT-ROOM room11 room12)
    (NEXT-ROOM room12 room13)
    (NEXT-ROOM room13 room14)
    (NEXT-ROOM room14 room15)
    (NEXT-ROOM room15 room1)
)
(:goal (and
    (slayer-is-alive)
    (not (vampire-is-alive))
    (slayer-is-in room13)
))
)
