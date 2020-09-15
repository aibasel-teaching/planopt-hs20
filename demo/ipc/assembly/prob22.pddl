(define (problem assem-x-22)
   (:domain assembly)
   (:objects mount sprocket-17 wire-59 coil-60 connector-61
             tube-62 thingumbob-63 whatsis-64 hoozawhatsie-22 foobar-18
             hack-19 contraption-20 socket-21 tube-25 fastener-23
             bracket-24 thingumbob-30 sprocket-26 contraption-27 widget-28
             device-29 bracket-13 connector-31 valve-32 frob-9 whatsis-10
             plug-11 unit-12 doodad-8 socket-14 coil-15 hoozawhatsie-7
             fastener-16 kludge-5 hack-6 hoozawhatsie wire-3 mount-4
             gimcrack-1 foobar-2 coil thingumbob socket bracket kludge frob
             gimcrack wire unit connector contraption device foobar hack tube
             valve widget whatsis fastener sprocket doodad plug
             - assembly
             hammer - resource)
   (:init (available wire-59)
          (available coil-60)
          (available connector-61)
          (available tube-62)
          (available thingumbob-63)
          (available whatsis-64)
          (available foobar-18)
          (available hack-19)
          (available contraption-20)
          (available socket-21)
          (available fastener-23)
          (available bracket-24)
          (available sprocket-26)
          (available contraption-27)
          (available widget-28)
          (available device-29)
          (available connector-31)
          (available valve-32)
          (available frob-9)
          (available whatsis-10)
          (available plug-11)
          (available unit-12)
          (available socket-14)
          (available coil-15)
          (available fastener-16)
          (available kludge-5)
          (available hack-6)
          (available wire-3)
          (available mount-4)
          (available gimcrack-1)
          (available foobar-2)
          (available coil)
          (available socket)
          (available bracket)
          (available kludge)
          (available frob)
          (available gimcrack)
          (available wire)
          (available contraption)
          (available device)
          (available hack)
          (available tube)
          (available widget)
          (available whatsis)
          (available fastener)
          (available sprocket)
          (available doodad)
          (available plug)
          (available hammer)
          (requires sprocket-17 hammer)
          (requires hoozawhatsie-22 hammer)
          (requires tube-25 hammer)
          (requires thingumbob-30 hammer)
          (requires doodad-8 hammer)
          (requires hoozawhatsie hammer)
          (requires thingumbob hammer)
          (requires unit hammer)
          (requires valve hammer)
          (part-of sprocket-17 mount)
          (part-of hoozawhatsie-22 mount)
          (part-of tube-25 mount)
          (part-of thingumbob-30 mount)
          (part-of bracket-13 mount)
          (part-of doodad-8 mount)
          (part-of hoozawhatsie mount)
          (part-of thingumbob mount)
          (part-of unit mount)
          (part-of valve mount)
          (part-of wire-59 sprocket-17)
          (part-of coil-60 sprocket-17)
          (part-of connector-61 sprocket-17)
          (part-of tube-62 sprocket-17)
          (part-of thingumbob-63 sprocket-17)
          (part-of whatsis-64 sprocket-17)
          (part-of foobar-18 hoozawhatsie-22)
          (part-of hack-19 hoozawhatsie-22)
          (part-of contraption-20 hoozawhatsie-22)
          (part-of socket-21 hoozawhatsie-22)
          (part-of fastener-23 tube-25)
          (part-of bracket-24 tube-25)
          (part-of sprocket-26 thingumbob-30)
          (part-of contraption-27 thingumbob-30)
          (part-of widget-28 thingumbob-30)
          (part-of device-29 thingumbob-30)
          (part-of connector-31 bracket-13)
          (part-of valve-32 bracket-13)
          (part-of frob-9 bracket-13)
          (part-of whatsis-10 bracket-13)
          (part-of plug-11 bracket-13)
          (part-of unit-12 bracket-13)
          (part-of socket-14 doodad-8)
          (part-of coil-15 doodad-8)
          (part-of hoozawhatsie-7 doodad-8)
          (part-of fastener-16 hoozawhatsie-7)
          (part-of kludge-5 hoozawhatsie-7)
          (part-of hack-6 hoozawhatsie-7)
          (part-of wire-3 hoozawhatsie)
          (part-of mount-4 hoozawhatsie)
          (part-of gimcrack-1 hoozawhatsie)
          (part-of foobar-2 hoozawhatsie)
          (part-of coil hoozawhatsie)
          (part-of socket thingumbob)
          (part-of bracket thingumbob)
          (part-of kludge thingumbob)
          (part-of frob thingumbob)
          (part-of gimcrack thingumbob)
          (part-of wire thingumbob)
          (part-of connector unit)
          (part-of foobar unit)
          (part-of contraption connector)
          (part-of device connector)
          (part-of hack foobar)
          (part-of tube foobar)
          (part-of widget valve)
          (part-of whatsis valve)
          (part-of fastener valve)
          (part-of sprocket valve)
          (part-of doodad valve)
          (part-of plug valve)
          (assemble-order sprocket-17 bracket-13 mount)
          (assemble-order hoozawhatsie valve mount)
          (assemble-order wire-59 tube-62 sprocket-17)
          (assemble-order connector-61 coil-60 sprocket-17)
          (assemble-order tube-62 coil-60 sprocket-17)
          (assemble-order tube-62 connector-61 sprocket-17)
          (assemble-order hack-19 socket-21 hoozawhatsie-22)
          (assemble-order hack-19 contraption-20 hoozawhatsie-22)
          (assemble-order fastener-23 bracket-24 tube-25)
          (assemble-order sprocket-26 widget-28 thingumbob-30)
          (assemble-order widget-28 device-29 thingumbob-30)
          (assemble-order widget-28 contraption-27 thingumbob-30)
          (assemble-order connector-31 valve-32 bracket-13)
          (assemble-order whatsis-10 connector-31 bracket-13)
          (assemble-order socket-14 hoozawhatsie-7 doodad-8)
          (assemble-order coil-15 hoozawhatsie-7 doodad-8)
          (assemble-order mount-4 coil hoozawhatsie)
          (assemble-order socket wire thingumbob)
          (assemble-order bracket gimcrack thingumbob)
          (assemble-order bracket frob thingumbob)
          (assemble-order connector foobar unit)
          (assemble-order contraption device connector)
          (assemble-order tube hack foobar)
          (assemble-order doodad sprocket valve))
   (:goal (complete mount)))