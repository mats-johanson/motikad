# Active Issues — Transalp

## Tach over-read

**Status:** investigating — next step: try pulse=2

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

---

## Fuel gauge lean-over dip

**Status:** understood — no fix needed, use Trip A as primary fuel gauge

**Observed:** the fuel gauge drops to empty for a while when the bike is leaned over (cornering or on the side stand).

**Cause:** physical, not electrical. The Honda fuel sender in the tank is a float-on-arm resistive sensor. When the bike leans, fuel sloshes to the low side of the tank. If the sender sits on the high side, the float drops into an empty pocket and the sender reports empty. The Koso is faithfully displaying what the sender sends. Nothing is wrong with the dash or the sender.

**Workaround — use Trip A as the primary fuel gauge:**

- Reset Trip A at every fill-up: on the main screen, press Adjust once to see Trip A, then hold Adjust 3s to reset.
- Tank capacity: 19.6 L. Consumption: 4.2–5.2 L/100km. Range: 280–350 km.
- **Rule of thumb: refuel by 250 km** and you always have reserve.
- Leave Trip B untouched as a trip/week accumulator.
- Treat the fuel bars as a secondary sanity check, not a source of truth.

**Not the same issue as** [stalls on side stand](todo.md) — that's actual fuel starvation at the pilot jets at extreme lean angle (a carburetor problem). Both involve fuel slosh in a tilted tank, but the fixes are unrelated: the gauge dip has no fix, the stall does.
