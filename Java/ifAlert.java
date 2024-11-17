import javafx.application.Application;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.scene.control.Alert.Alerttype;
import javafx.stage.Stage;

public class ifAlert extends Application{
    public void start(Stage stage){
        CheckBox cb1 = new CheckBox("English");
        CheckBox cb2 = new CheckBox("Physics");
        CheckBox cb3 = new CheckBox("DBMS");
        CheckBox cb4 = new CheckBox("CS");
        Button b1= new Button("Submit");
        Label l1= new Label();
        VBox root = new VBox("CheckBox");
        root.getChildern().addAll(cb1,cb2,cb3,cb4,b1,l1);

                
    }
}


