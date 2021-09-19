from ex4 import mot_possible,mot_possible2
import time

def calculer_temps_traitement(fonciton_to_test:callable):
    time_start = time.perf_counter_ns()
    fonciton_to_test("lapin","abilnqp")
    time_end = time.perf_counter_ns()
    return time_end - time_start

print(
    calculer_temps_traitement(
        mot_possible
    )
)
