import javafx.application.Application;
import javafx.scene.Scene;
import javafx.event.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.stage.Stage;


class Gpane extends Application{
    @Override
    public void start(Stage PrimaryStage){
        Label fname = new Label("F name");
        Label lname = new Label("L name");
        TextField tf1 = new TextField();
        TextField tf2 = new TextField();
        Button b1 = new Button("Submit");
        GridPane gp = new GridPane();
        Scene scene = new Scene(gp,500,300);
        gp.addRow(0,fname,tf1);
        gp.addRow(1,lname,tf2);
        gp.addRow(2,b1);
        PrimaryStage.setScene(scene);
        PrimaryStage.show();
              


    }


    public static void main(String[] args){
        launch(Gpane.class);
               
    }
}
                             
