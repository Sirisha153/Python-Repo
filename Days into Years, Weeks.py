import java.util.Scanner;
public class DaysintoYearsWeeks
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int D=sc.nextInt();
        int Years = D/365;
        int Weeks =(D%365)/7;
        System.out.println(Years);
        System.out.println(Weeks);
    }
}