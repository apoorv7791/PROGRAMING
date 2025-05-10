import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class rehab extends JFrame implements ActionListener, java.awt.event.ActionListener {
    JPanel p;
    JLabel username, password, message;
    JTextField username_text;
    JPasswordField password_text;
    JButton submit, cancel;

    rehab() {
        // Username label
        username = new JLabel();
        username.setText("Welcome");
        username_text = new JTextField();

        // Password label
        password = new JLabel();
        password.setText("Password");
        password_text = new JPasswordField();

        // submit
        submit = new JButton("SUBMIT");

        p = new JPanel(new GridLayout(3, 1));
        p.add(username);
        p.add(username_text);
        p.add(password);
        p.add(password_text);

        message = new JLabel();
        p.add(message);
        p.add(submit);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        submit.addActionListener(this);
        add(p, BorderLayout.CENTER);
        setTitle("Please Login");
        setSize(430, 350);
        setVisible(true);
    }

    public static void main(String[] args) {
        new rehab();
    }

    public void actionperformed(ActionEvent ae) {
        String username = "Apoorv";
        String password = "redemption123456";
        if (username.trim().equals("Apoorv") && password.trim().equals("redemption123456")) {
            message.setText("hello" + username + "");
        } else {
            message.setText("Invalid");
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        throw new UnsupportedOperationException("Unimplemented method 'actionPerformed'");
    }
}
