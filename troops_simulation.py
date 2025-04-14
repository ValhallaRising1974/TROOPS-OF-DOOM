
# troops_simulation.py

from ghost_s_4 import GhostS4
from squeleton_s_4 import SqueletonS4
from crab_s_2 import CrabS2
from snail_s_2 import SnailS2
from aracno_ss import AracnoSS
from zoombie_ss import ZoombieSS

def simulate_wave():
    print("=== Standard Troops ===")
    ghosts = GhostS4()
    print(f"{ghosts.quantity}x {ghosts.name} attack: {ghosts.attack()} ({ghosts.special})")

    skeletons = SqueletonS4()
    print(f"{skeletons.quantity}x {skeletons.name} attack: {skeletons.attack()}")

    print("\n=== Support Troops ===")
    crabs = CrabS2()
    print(f"{crabs.quantity}x {crabs.name} absorb damage: {crabs.absorb(100)}")

    snails = SnailS2()
    print(f"{snails.quantity}x {snails.name} healing ability: {snails.heal()}")

    print("\n=== Superminions (Endgame) ===")
    aracno = AracnoSS()
    print(f"{aracno.name} special move: {aracno.charge()}")

    zoombie = ZoombieSS()
    print(f"{zoombie.name} ultimate slam: {zoombie.smash()}")

if __name__ == "__main__":
    simulate_wave()
