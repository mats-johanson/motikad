# Reference — Transalp

* {:toc}

**Docs:** [Service Manual](docs/service-manual.pdf) · [KOSO DB-01R+ Manual](docs/koso-db01r-manual.pdf)

## Cold-start protocol

Choke on → start → 30–60s until idle smooths → gradually push choke off → ride gently first few minutes.

## Modifications (custom build, appearance modified 2021)

| Component | Mod | Notes |
|-----------|-----|-------|
| Headers | Arrow 72068PD | — |
| Muffler | Mivv Suono Steel Black H.023.L9 | — |
| Rims | Excel 17" front + rear | Both 17" — supermoto/street scrambler config, NOT stock 21"/17" ADV setup |
| Tires | Mitas E-09 Dakar TL 120/90-17 (F), 150/70-17 (R) | — |
| Front forks | KTM units (SM690?) | Replaces soft stock 41mm Honda forks. Requires triple clamp/axle spacer work |
| Speedometer | KOSO DB-01R+ | Digital, replaces stock cluster. [Manual](docs/koso-db01r-manual.pdf) |
| Handlebar risers | RAXIMO TÜV 28.6mm +50mm | — |
| Heated grips | Daytona 4-Stage | Integrated controller |
| Headlight | Flashpoint LED 7" | — |
| Mirrors | Daytona CNC Hexagon Aluminium | — |
| Levers | AVDB short (brake + clutch) | — |
| Front brake disc | Brembo Serie Oro 68B407M4 | — |
| Rear brake disc | TRW MST347 | — |
| Front sprocket | JTF1307.15RB (15T, 520, rubber cushioned) | — |
| Rear sprocket | JTR853.48 (48T, 520) | — |
| Chain | DID 520 VX3 Gold & Black, 118 links | — |
| USB charger | Daytona slim-mount | — |
| Battery | Gel type | — |
| Seat | Custom | — |
| Bodywork | Custom stripped/restyled | Stock plastics removed |
| Side stand foot extension | — | — |
| Givi tool box | S250 + S250KIT | — |

## Known Model Characteristics

**Strengths:** Honda V-twin reliability, comfortable touring ergonomics, good fuel range (280–350 km on 19.6L tank), huge global parts availability (shares engine with Deauville), capable on light off-road.

**Weaknesses:** Lackluster brakes, soft stock suspension (front addressed via KTM fork swap), 52hp adequate but modest on highways, valve clearance service requires bent feeler gauge (front cyl), carbs can clog if bike sits, wheel bearings and swingarm/linkage bearings wear in wet/salty climates.

## Fuel & Range

- **Tank:** 19.6L
- **Consumption:** 4.2–5.2 L/100km
- **Range:** 280–350 km (gentle touring ~350, spirited ~280)
- Aftermarket exhaust may increase consumption slightly

## Stock Specs vs. This Bike

| Spec | Stock | This bike |
|------|-------|-----------|
| Front wheel | 21" (90/90-21) | 17" Excel |
| Rear wheel | 17" (120/90-17) tube | 17" Excel |
| Front suspension | 41mm telescopic, unadjustable, 200mm travel | KTM forks |
| Rear suspension | Pro-Link, compression adj, 172mm travel | Stock (age: 23 years) |
| Front brakes | 2x 256mm disc, 2-piston | Brembo Serie Oro disc + LA pads |
| Rear brake | 240mm disc, 1-piston | Stock |
| ABS | None (no XL650V had ABS) | — |
| Dry weight | 191 kg | — |
| Seat height | 843mm | — |

## KOSO DB-01R+ Digital Dash

Replaces the stock cluster. Two buttons: **Adjust** (left) and **Select** (right). DC 12V, standalone.

### Button map — daily use

| Screen     | Adjust (short) | Adjust (3s hold) | Select (short)       | Select (3s hold)     |
|------------|----------------|------------------|----------------------|----------------------|
| Main       | → Trip         | —                | Cycle backlight colour | Toggle km/h ↔ MPH  |
| Trip A/B   | → Clock        | Reset trip       | Cycle backlight      | —                    |
| Clock      | → Main         | —                | Cycle backlight      | —                    |

- **Backlight colours:** blue → orange → purple → blue …
- **Trip reset** only works while viewing the trip screen.
- **Setting mode:** hold **Adjust + Select together for 3 seconds** on the main screen.

### Cool features

1. **Trip A + Trip B independently** — use A for the current tank, B for the current trip/tour.
2. **Km/h ↔ MPH** on a 3-second hold of Select — handy for UK.
3. **Clock with persistent power** — stays set if Red wire is on permanent +12V.
4. **Backlight colour change** without entering settings — Select, one tap.

<details markdown="1">
<summary>KOSO setting sequence (10 steps)</summary>

Enter setting mode with **Adjust + Select (3s)**. Each step: **Adjust** changes the value, **Select** moves to the next digit and then to the next step.

| # | Setting             | Value for this bike                        | Notes                                                    |
|---|---------------------|--------------------------------------------|----------------------------------------------------------|
| 1 | Clock — hour        | Local (Tartu: EET winter / EEST summer)    | 0–23                                                     |
| 2 | Clock — minute      | Local                                      | 0–59                                                     |
| 3 | Tire circumference  | **2065 mm**                                | Confirmed accurate vs GPS — do not change                |
| 4 | Sensor points       | **1** (one magnet on the wheel)            | Koso allows 1–99 on the dial, passive sensor max is 20; this bike uses 1 |
| 5 | RPM pulse           | Book: **1** (4C-2P) — but over-reads on this bike | See [issues → Tach over-read](issues.md#tach-over-read) |
| 6 | RPM polarity        | Start **Hi**, fall back to **Lo**          | If tach stays at 0, toggle to Lo and re-check            |
| 7 | Bar graph tach range| **10,000 RPM**                             | XL650V redline ≈ 8,500, peak power @ 7,500               |
| 8 | Fuel gauge resistance | **100 Ω**                                | Honda spec: 9.3 Ω full / 92.3 Ω empty — nearest is 100 Ω |
| 9 | Internal odometer   | Current value (or leave)                   | Accumulates automatically                                |
|10 | External odometer   | Set to real bike odo at install            | So the Koso matches the bike's actual km                 |

</details>

<details markdown="1">
<summary>KOSO wiring reference</summary>

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

</details>

<details markdown="1">
<summary>Tire circumference & speed sensor</summary>

Current setting: **2065 mm** (previous owner, confirmed accurate against GPS — leave alone).

If the wheel/tire is ever replaced, re-measure:

1. Pump tires to normal touring pressure.
2. Sit on the bike (loaded circumference < unloaded).
3. Mark the tire tread at the contact patch with chalk, mark the ground below.
4. Roll straight forward one full rotation.
5. Measure the distance between ground marks in **mm**.
6. Enter in step 3 of the setting sequence.

**Sanity-check ballparks** (unloaded, expect ~2–3% less loaded):

| Tire (installed) | Calc OD  | Calc circumference | Expected loaded |
|------------------|----------|--------------------|-----------------|
| 120/90-17 front  | 647.8 mm | ~2035 mm           | ~1975 mm        |
| 150/70-17 rear   | 641.8 mm | ~2016 mm           | ~1955 mm        |

The speed sensor uses **1 magnet** (sensor point = 1), needs ≤2 mm gap. Reads accurately against GPS. To verify: turn wheel by hand — dash should register.

</details>

## Troubleshooting — Koso dash

| Symptom                               | First check                                                              |
|---------------------------------------|--------------------------------------------------------------------------|
| Dash dead with ignition on            | Red (+12V), Brown (key-on), Black (ground) — all must be connected; fuse intact |
| Wrong/garbled readouts                | Battery < 12V — charge or replace                                        |
| Speed reads 0 or wrong                | Sensor-to-magnet distance > 2 mm; wrong sensor points count; wrong tire circumference |
| Tach reads 0 or erratic               | RPM wire on wrong colour (should be coil +, Yellow/Green on Honda); try flipping Hi/Lo polarity; check RPM pulse = 1 |
| Fuel gauge blank or stuck             | Wiring wrong; resistance setting wrong (should be 100 Ω); stock sender failed — measure sender Ω with multimeter: expect ~9 Ω full, ~92 Ω empty |
| Fuel gauge dips to empty when leaned  | **Normal** — sender float slosh. Not a fault. See [issues → Fuel gauge lean-over dip](issues.md#fuel-gauge-lean-over-dip) |
| Tach reads too high despite correct pulse setting | See [issues → Tach over-read](issues.md#tach-over-read) |
| Odometer / trip doesn't accumulate    | Red (permanent +12V) not connected well — trip counter loses state on key-off |
| Clock resets every key cycle          | Red is on switched power instead of permanent +12V — swap to the always-hot side of the fuse box |

## Odometer Reconciliation

| Source                                   | Value       | What it represents                          |
|------------------------------------------|-------------|---------------------------------------------|
| Maanteeamet last ARK inspection (~2024)  | 68,000 km   | Last officially recorded value              |
| Koso external odometer (setup step 10)   | 72,663 km   | Previous owner's manual total               |
| Koso main-screen odometer (internal)     | 42,344 km   | Distance counted since Koso install         |

**Best current estimate of real total mileage: ~72,000 km.** Treat as the working total until the next ARK inspection (05/2026).

**Do not** use the main-screen ODO as the bike's real total — it's only the Koso's own accumulator since install.

<details markdown="1">
<summary>Accident history</summary>

**05 September 2024 — Tallinn.** Toyota Corolla (100% at fault) knocked into the bike. Repairs by M&M Motorcycles OÜ (Motorem), [invoice #2048](docs/motorem-invoice-2048.jpg) — **€2,968** covering radiator, exhaust, handlebar, fork repair/straightening, tank painting, engine case cover, engine guard, footpegs, brake/shift pedals, and disassembly/reassembly. Compensation via Swedbank P&C Insurance. Passed ARK inspection post-accident.

</details>

<details markdown="1">
<summary>Intended use & seller info</summary>

**Intended use:**
- Gravel and light off-road (beginner level)
- Weekend trips, 1–2 week European touring
- Possible TET sections with friend on Honda Varadero

**Seller:**
- Reimo Ranniku, +372 5806 2883, via mototehnika.ee
- [YouTube video of bike](https://www.youtube.com/watch?v=XrkYIXr79WE)

</details>
