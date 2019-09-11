import java.util.ArrayList;
import RandomGenerator;

private final int NUM_TESTS = 1000;
private final int TARGET = 750;

public static void main(String[] args)
{
    ArrayList uniqueSamples = new ArrayList();
    RandomGenerator rg = new RandomGenerator();
    int randNum = 0;
    boolean successful = false;

    for (int i = 0; i < NUM_TESTS; i++)
    {
	randNum = rg.generateRandNum();

	if (!uniqueSamples.contains(randNum))
	{
	    uniqueSamples.add(randNum);
	}

	if (uniqueSamples.size() >= TARGET)
	{ 
	    successful = true;
	    break;
	}
    }

    System.out.println("Test Results:");

    if (successful)
	System.out.println("Successful");
    else
	System.out.prinln("Unsuccessful. Generated only " + uniqueSamples.size() + "/" + TARGET + " unique numbers");

}