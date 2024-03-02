import javax.swing.JFrame;
import java.awt.Color;

/**
 * Class that contains the main method for the program and creates the frame containing the component.
 */
public class SolarSystemViewer
{
    // the cityscape will be animated for 60 seconds
    static final int ANIMATION_TIME_IN_SECONDS = 60;
   
    /**
     * main method for the program which creates and configures the frame for the program
     * 
     * @param args  not used
     *
     */
    public static void main(String[] args) throws InterruptedException
    {
        // create and configure the frame (window) for the program
        JFrame frame = new JFrame();
        
        Color night = new Color(80,85,137);
        
        frame.setSize(700 /* x */, 500 /* y */);
        
        frame.setTitle("Cityscape");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // a frame contains a single component; create the Cityscape component and add it to the frame
        CityscapeComponent component = new CityscapeComponent();
        frame.add(component);
        
        frame.getContentPane().setBackground(night);
        // make the frame visible which will result in the paintComponent method being invoked on the
        //  component.
        frame.setVisible(true);
        
        // animate the cityscape
        for( int seconds = 0; seconds < ANIMATION_TIME_IN_SECONDS; seconds++ )
        {
            component.nextFrame();
            Thread.sleep( 1000 );
        }
        
    }

}