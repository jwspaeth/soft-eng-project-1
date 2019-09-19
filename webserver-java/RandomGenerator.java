import java.lang.Math;

public class RandNumGenerator
{
    public int generateRandNum()
    {
	return (int) (Math.random() * 1000000);
    }
}
