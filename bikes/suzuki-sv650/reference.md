# Reference — SV650

* {:toc}

**Docs:** [Service Manual](docs/service-manual/) · [Wiring Diagram](docs/service-manual/SV650S-E03-wiring.pdf) · [Torque Specs](docs/service-manual/sv650TorqueSpecs.pdf)

## Known Model Quirks

- **Dual-spark (2007+):** 4 plugs, not 2. Both plugs per cylinder fire simultaneously.
- **No chassis ground:** Aluminium frame — all grounds via wiring harness (black/white wires) back to battery. Main ground: battery negative → 8mm engine case bolt in front of swingarm.
- **No spark plug drain hole** on 2007+ dual-spark heads. Dual-spark design is Suzuki's fix for water ingress — if top plug drowns, side plug keeps firing.
- **Regulator/rectifier:** Known failure point on gen 2. Currently fine (14.5V). Inspect periodically.
- **V-twin idle character:** Uneven firing order by design. Slight lumpiness is normal.
- **Headlight bracket clamps** can slide on smooth chrome fork tubes — fix with rubber shim.

## Dual-Spark Ignition (2007+)

- 4 plugs total, 2 per cylinder (top + side)
- Both plugs per cylinder fire simultaneously
- Disconnecting one plug shows no idle change — must disconnect both on same cylinder to hear a difference
- No spark plug drain hole on 2007+ heads — dual-spark design is Suzuki's fix for water ingress
- Pack plug boots with dielectric grease for rain protection

## Spark Plug Access

- **Rear top:** straightforward
- **Front right:** straightforward
- **Front top (behind radiator):** loosen radiator (unbolt, push forward, don't drain), thin-wall 16mm socket + extension
- **Rear side:** lift fuel tank, tight space
- Torque: <10 ft-lb, always finger-thread first (aluminium heads)

## Grounding System

- Aluminium frame — no chassis ground (galvanic corrosion risk)
- All grounds via wiring harness, black/white stripe wires, back to battery
- Main ground cable: battery negative → 8mm engine case bolt in front of swingarm
- Bad grounds cause voltage spikes that kill LEDs
- Cleaning the rear ground junction under seat fixed intermittent brake light flickering

## OEM Flasher Relay

- 7-pin thermal/bimetallic relay under seat
- Needs incandescent-level current to heat bimetallic strip and cycle
- LEDs alone: not enough current → no flash
- With resistors: hazards OK (4 signals = enough load), single-side hyperflash (2 signals = half load)
- LED relay fix: electronic relay flashes regardless of load, remove resistors after install

## Idle

- Spec: 1200–1300 RPM
- Adjuster: knob on left side of throttle body area
- Counter-clockwise = lower RPM
- 90° V-twin has uneven firing order by design — slight lumpiness is normal, not a misfire

## Exhaust

- Aftermarket Akrapovic knockoff, carbon fiber look, flared/funnel tip
- 48mm internal diameter, straight (not angled)
- ~150mm available depth
- Screw hole on bottom for DB killer retention bolt
- DB killer adjustable: cap at innermost hole = quietest, cap at tip = louder but controlled
- Less backpressure with aftermarket exhaust → rear cylinder runs slightly rich (sooty plug, normal)

## Regulator/Rectifier

- Known failure point on gen 2 SV650
- Currently healthy: 14.5V running
- Inspect periodically — failure causes overcharging or undercharging
