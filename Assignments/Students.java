
protected class JavaStudents {

    String name, laptop_name;
    int id;

    public JavaStudents() {
        name = "Lucky";
        laptop_name = "Dell";
        id = 1119;
    }

    public void printInfo() {
        System.out
                .println("The name is " + " " + name + " " + "using" + " " + laptop_name + " " + "with ID " + " " + id);
    }

}

public class Students extends JavaStudents {
    void printline() {
        printinfo();
    }

    public static void main(String[] args) {
        Students st = new Students();
        st.printline();
    }
}
