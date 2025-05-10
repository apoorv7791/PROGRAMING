class real{
    float salary = 40000;
}
class employee extends real{
    int bonus = 10000;
    public static void main(String[] args) {
        employee e = new employee();
        System.out.println("Programmer's salary is :"+e.salary);
        System.out.println("Bonus salary is :"+e.bonus);
    }
}