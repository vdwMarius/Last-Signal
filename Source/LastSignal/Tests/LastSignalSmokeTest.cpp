// M00 disposable automation test: proves the automation runner discovers and
// executes project tests. Replace or remove once M01 adds real coverage.
#include "Misc/AutomationTest.h"

#if WITH_DEV_AUTOMATION_TESTS

IMPLEMENT_SIMPLE_AUTOMATION_TEST(FLastSignalSmokeTest, "LastSignal.Preflight.Smoke",
	EAutomationTestFlags::EditorContext | EAutomationTestFlags::EngineFilter)

bool FLastSignalSmokeTest::RunTest(const FString& Parameters)
{
	TestTrue(TEXT("Automation runner executes project tests"), true);
	return true;
}

#endif
