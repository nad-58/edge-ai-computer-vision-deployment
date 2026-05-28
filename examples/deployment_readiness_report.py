from edge_ai.deployment_checklist import deployment_readiness_score


def main() -> None:
    checks = {
        "representative_validation_data": True,
        "latency_target_met": True,
        "memory_budget_met": True,
        "quantisation_drop_acceptable": True,
        "robustness_tests_completed": False,
        "hardware_integration_tested": True,
        "release_plan_defined": False,
    }

    result = deployment_readiness_score(checks)

    print("Deployment readiness report")
    print("===========================")
    print(result)

    if result["ready_for_release"]:
        print("\nDecision: ready for release")
    else:
        print("\nDecision: further work required before release")
        print("Open checks:")
        for check_name in result["failed_checks"]:
            print(f"- {check_name}")


if __name__ == "__main__":
    main()
