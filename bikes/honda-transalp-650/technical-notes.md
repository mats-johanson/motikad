[← Home](../../README.md) · [Bike](README.md) · [Maintenance](maintenance.md) · [Parts](parts.md) · [Shops](../../shops.md) · [Riding](../../riding/routes.md)

**Docs:** [Service Manual](docs/service-manual.pdf) · [KOSO DB-01R+ Manual](docs/koso-db01r-manual.pdf)

# Technical Notes — 2003 Honda XL650V Transalp

## KOSO DB-01R+ Digital Dash

Replaces the stock cluster. Two buttons: **Adjust** (left) and **Select** (right). The unit is DC 12V, standalone — it gets power, ignition, ground, RPM from the coil, speed from a magnet+sensor on a wheel, fuel from the stock sender, plus optional inputs for indicator lights.

### Button map — daily use

| Screen     | Adjust (short) | Adjust (3s hold) | Select (short)       | Select (3s hold)     |
|------------|----------------|------------------|----------------------|----------------------|
| Main       | → Trip         | —                | Cycle backlight colour | Toggle km/h ↔ MPH  |
| Trip A/B   | → Clock        | Reset trip       | Cycle backlight      | —                    |
| Clock      | → Main         | —                | Cycle backlight      | —                    |

- **Backlight colours:** blue → orange → purple → blue …
- **Trip reset** only works while viewing the trip screen.
- **Setting mode:** hold **Adjust + Select together for 3 seconds** on the main screen. If no button is pressed for 30 seconds inside settings, the unit returns to the main screen.

### Indicator lights

| Icon          | Colour | Wire to                          |
|---------------|--------|----------------------------------|
| High beam     | Blue   | Yellow → +12V high beam          |
| Low beam      | —      | Green/Yellow → +12V low beam     |
| Turn signal L | Green  | Orange → +12V L turn             |
| Turn signal R | Green  | Blue → +12V R turn               |
| Neutral       | Green  | White → neutral switch (–)       |
| Oil           | Red    | Gray → oil switch (+ / –)        |
| Fuel reserve  | Yellow | Red/White fuel signal + Green (–)|
| Engine check  | Yellow | Purple → EOBD (–)                |

### Power/signal wiring — Honda reference

| Signal            | Koso wire       | Honda wire colour    |
|-------------------|-----------------|----------------------|
| Battery +12V      | Red             | Red                  |
| Key-on (ignition) | Brown           | Red/Black            |
| Ground            | Black           | Green                |
| RPM pickup        | Brown/Red       | Yellow/Green (coil +)|
| Fuel sender       | Red/White + Green | Yellow/White + ground |

> The fuel sender wire must **not** be paralleled with the stock gauge — Koso is electronic and will be destroyed. Cut the original feed and reroute to the Koso, or remove the stock gauge circuit entirely.

### Setting sequence (10 steps)

Enter setting mode with **Adjust + Select (3s)**. Each step: **Adjust** changes the value, **Select** moves to the next digit and then to the next step.

| # | Setting             | Value for this bike                        | Notes                                                    |
|---|---------------------|--------------------------------------------|----------------------------------------------------------|
| 1 | Clock — hour        | Local (Tartu: EET winter / EEST summer)    | 0–23                                                     |
| 2 | Clock — minute      | Local                                      | 0–59                                                     |
| 3 | Tire circumference  | **2065 mm**                                | Confirmed accurate vs GPS — do not change                |
| 4 | Sensor points       | **1** (one magnet on the wheel)            | Koso allows 1–99 on the dial, passive sensor max is 20; this bike uses 1 |
| 5 | RPM pulse           | Book: **1** (4C-2P) — but over-reads on this bike | See [Known issues → Tach over-read](#tach-over-read) |
| 6 | RPM polarity        | Start **Hi**, fall back to **Lo**          | If tach stays at 0, toggle to Lo and re-check            |
| 7 | Bar graph tach range| **10,000 RPM**                             | XL650V redline ≈ 8,500, peak power @ 7,500               |
| 8 | Fuel gauge resistance | **100 Ω**                                | Honda spec: 9.3 Ω full / 92.3 Ω empty — nearest is 100 Ω |
| 9 | Internal odometer   | Current value (or leave)                   | Accumulates automatically                                |
|10 | External odometer   | Set to real bike odo at install            | So the Koso matches the bike's actual km                 |

### Tire circumference — reference

Current setting: **2065 mm** (previous owner, confirmed accurate against GPS — leave alone).

If the wheel/tire is ever replaced, re-measure with this procedure:

1. Pump tires to normal touring pressure.
2. Sit on the bike (loaded circumference < unloaded).
3. Mark the tire tread at the contact patch with chalk, and mark the ground directly below it.
4. Roll the bike straight forward until the same chalk mark is back at the bottom (one full rotation).
5. Mark the ground at the new contact patch. Measure the distance between the marks in **mm**.
6. Enter the number in step 3 of the setting sequence.

**Sanity-check ballparks** (unloaded geometry, expect ~2–3% less loaded):

| Tire (installed) | Calc OD  | Calc circumference | Expected loaded |
|------------------|----------|--------------------|-----------------|
| 120/90-17 front  | 647.8 mm | ~2035 mm           | ~1975 mm        |
| 150/70-17 rear   | 641.8 mm | ~2016 mm           | ~1955 mm        |

The actual 2065 mm reading is slightly above both ballparks — consistent with a slightly over-rolled measurement or a near-new tire at the high end of tolerance. Either way, GPS says it's right.

### Speed sensor — how it's set up on this bike

The Koso passive sensor needs a magnet within ≤2 mm of the sensor tip. This bike is configured with **1 magnet** (sensor point = 1) and **tire circumference 2065 mm**, and reads accurately against GPS.

At 100 km/h the sensor sees ~13.5 pulses/sec (1 pulse per 2065 mm of travel), which is well within the passive sensor's capability. At very low speeds (walking pace) the update rate is ~0.5 Hz, so expect a slightly coarse/laggy reading when crawling — this is the normal tradeoff of a single-magnet setup.

If you ever want smoother low-speed readings, more magnets can be added — the passive sensor supports up to 20 points per rotation. You'd then update sensor points in step 4 to match the new physical count, and tire circumference stays the same.

To verify the sensor is working: turn the wheel by hand — the dash should register. If not, check distance to magnet and try flipping the sensor polarity.

### Cool features worth using

1. **Trip A + Trip B independently** — use A for the current tank, B for the current trip/tour. Reset each as needed without losing the other.
2. **Km/h ↔ MPH** on a 3-second hold of Select — handy if crossing into the UK.
3. **Clock with persistent power** — set once and it stays, as long as the Red wire is on permanent +12V (not switched). If the clock resets on every key-off, the Red wire is wrong.
4. **Backlight colour change** without entering settings — Select, one tap, day/night/mood.
5. **10/12/15k RPM selectable scale** — if you ever put the same dash on a higher-revving bike (SV650, say), just change step 7.
6. **Engine check light wired to Purple/EOBD** — on a carbureted XL650V there's no OBD, so this LED is effectively a free indicator you could repurpose for anything 12V (e.g. fuel pump, aux light, low oil pressure) by wiring it through an extra switch/relay.

## Troubleshooting — Koso dash

| Symptom                               | First check                                                              |
|---------------------------------------|--------------------------------------------------------------------------|
| Dash dead with ignition on            | Red (+12V), Brown (key-on), Black (ground) — all must be connected; fuse intact |
| Wrong/garbled readouts                | Battery < 12V — charge or replace                                        |
| Speed reads 0 or wrong                | Sensor-to-magnet distance > 2 mm; wrong sensor points count; wrong tire circumference |
| Tach reads 0 or erratic               | RPM wire on wrong colour (should be coil +, Yellow/Green on Honda); try flipping Hi/Lo polarity; check RPM pulse = 1 |
| Fuel gauge blank or stuck             | Wiring wrong; resistance setting wrong (should be 100 Ω); stock sender failed — measure sender Ω with multimeter: expect ~9 Ω full, ~92 Ω empty |
| Fuel gauge dips to empty when leaned  | **Normal** — sender float slosh. Not a fault. See [Known issues → Fuel gauge lean-over dip](#fuel-gauge-lean-over-dip) |
| Tach reads too high despite correct pulse setting | See [Known issues → Tach over-read](#tach-over-read) |
| Odometer / trip doesn't accumulate    | Red (permanent +12V) not connected well — trip counter loses state on key-off |
| Clock resets every key cycle          | Red is on switched power instead of permanent +12V — swap to the always-hot side of the fuse box |

## Known issues on this bike

### Tach over-read

**Observed (2026-04-08):** tach reads ~1.5× higher than reality.

| Condition             | Koso shows   | Likely actual | Factor |
|-----------------------|--------------|---------------|--------|
| Warm idle             | 2,000 RPM    | ~1,300 RPM    | ~1.54  |
| Cold idle (choke on)  | 3,000 RPM    | ~1,900 RPM    | ~1.58  |
| Full revs             | pegs 10k+    | ~8,500 redline| ~1.5   |

**Confirmed correct settings:**
- Pulse = 1 (book value for 4C-2P, 4-stroke V-twin)
- Polarity = Hi
- Bar range = 10,000 RPM

**What was tried:**
- Changed pulse from 1 → **1.5**. Verified the setting saved (re-entered settings menu, saw 1.5). Idle reading **did not change** from 2,000 RPM. This rules out a simple pulse-multiplier error — if pulse values affected the display linearly, going from 1 to 1.5 should have dropped the reading by ~33%. It didn't move at all.

**Interpretation:** The Koso may be treating 1.5 as a no-op (no engine type mapped to it in the manual's table), or the tach isn't deriving its reading from the actual coil pulse frequency at all. Either way, the fix is not likely a software-only setting tweak.

**Next steps to try, in order:**

1. **Pulse = 2.** This corresponds to a valid engine type (4C-4P) and should *definitely* halve the reading if the setting does anything. If idle drops from 2,000 to ~1,000 → the setting system works but the correct value is somewhere else (try 1.5 again, or accept the 2x and note the scale). If idle still shows 2,000 → the Koso isn't reading pulse count, and the fix is hardware.
2. **Polarity Lo.** Toggle step 6 from Hi → Lo and see if reading changes at all. If it goes to 0, wrong polarity. If it goes erratic, signal noise.
3. **Confirm spark plugs are R-type.** XL650V OEM is NGK DPR8EA-9 — the "R" is the resistor. Non-resistor plugs cause RFI that the Koso tach circuit picks up as extra pulses. The Koso manual explicitly calls this out. Pull a plug and check the part number.
4. **Trace the RPM wire back to its tap.** The book assumes the tap is on *one* coil + pin. If this install is on a shared +12V bus feeding both coils, the Koso sees both coils' pulses and over-reads. Fix = move the tap to the + pin of a single coil.
5. **Check for noise pickup.** If the RPM wire runs near HT leads or the coil secondaries, capacitive coupling can inject extra pulses. Reroute or shield.
6. **Verify real idle with an independent source** — a timing-light tach or the front cylinder's coil output on a scope — to confirm what the actual idle RPM is and how far off the Koso really is.

### Fuel gauge lean-over dip

**Observed:** the fuel gauge drops to empty for a while when the bike is leaned over (cornering or on the side stand).

**Cause:** physical, not electrical. The Honda fuel sender in the tank is a float-on-arm resistive sensor. When the bike leans, fuel sloshes to the low side of the tank. If the sender sits on the high side, the float drops into an empty pocket and the sender reports empty. The Koso is faithfully displaying what the sender sends. Nothing is wrong with the dash or the sender.

**Workaround — use Trip A as the primary fuel gauge:**

- Reset Trip A at every fill-up: on the main screen, press Adjust once to see Trip A, then hold Adjust 3s to reset.
- Tank capacity: 19.6 L. Consumption: 4.2–5.2 L/100km. Range: 280–350 km.
- **Rule of thumb: refuel by 250 km** and you always have reserve.
- Leave Trip B untouched as a trip/week accumulator.
- Treat the fuel bars as a secondary sanity check, not a source of truth.

**Not the same issue as** [stalls on side stand](maintenance.md) — that's actual fuel starvation at the pilot jets at extreme lean angle (a carburetor problem). Both involve fuel slosh in a tilted tank, but the fixes are unrelated: the gauge dip has no fix, the stall does.

### Odometer reconciliation

The Koso main-screen ODO is not the bike's real lifetime mileage. There are three numbers:

| Source                                   | Value       | What it represents                          |
|------------------------------------------|-------------|---------------------------------------------|
| Maanteeamet last ARK inspection (~2024)  | 68,000 km   | Last officially recorded value              |
| Koso external odometer (setup step 10)   | 72,663 km   | Previous owner's manual total               |
| Koso main-screen odometer (internal)     | 42,344 km   | Distance counted since Koso install         |

**Best current estimate of real total mileage: ~72,000 km.** The Koso external value is plausible if the previous owner rode ~4,600 km between the 2024 inspection and the sale. Treat it as the working total until the next ARK inspection (05/2026) provides a new officially recorded number.

**Do not** use the main-screen ODO as the bike's real total — it's only the Koso's own accumulator since install.
