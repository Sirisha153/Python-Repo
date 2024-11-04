import java.util.Scanner;
public class Findtheaverageoftwonumbers
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        double num1=sc.nextDouble();
        double num2=sc.nextDouble();
        double avg=(num1+num2)/2;
        System.out.printf("%.4f%n",avg);
        sc.close();
    }
}