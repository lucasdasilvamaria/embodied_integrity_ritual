from app.logic.ritual_tracker import log_ritual_step

def main():
    print("🌀 Embodied Integrity Ritual Tracker")
    step = input("Which ritual step did you complete? ")
    notes = input("Notes or reflections? ")
    log_ritual_step(step, notes)
    print("✅ Step logged. Stay strong, hermano.")

if __name__ == "__main__":
    main()