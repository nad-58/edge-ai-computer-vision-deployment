from edge_ai.latency import latency_acceptance, latency_summary


def main() -> None:
    devices = {
        "embedded_cpu": [42.0, 39.5, 41.2, 44.1, 40.8, 43.0],
        "edge_gpu": [11.4, 10.9, 12.1, 11.8, 10.7, 12.5],
        "optimised_runtime": [18.2, 17.6, 19.1, 18.9, 17.9, 19.4],
    }

    target_ms = 25.0

    print("Model latency report")
    print("====================")
    for device_name, measurements in devices.items():
        summary = latency_summary(measurements)
        acceptance = latency_acceptance(summary, target_ms=target_ms)
        print(f"\nDevice: {device_name}")
        print(summary)
        print(acceptance)


if __name__ == "__main__":
    main()
