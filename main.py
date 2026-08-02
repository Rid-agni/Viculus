from src.world.clock import Clock

def main():
    clock = Clock()

    for _ in range(10):
        print(clock.current_time())
        clock.tick()
if __name__ == "__main__":
    main()