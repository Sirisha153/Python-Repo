import java.util.Scanner;
public class RequiredPoints
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int A=sc.nextInt();
        int B=sc.nextInt();
        int num=B/A;
        System.out.println(+num);
        sc.close();
    }
}