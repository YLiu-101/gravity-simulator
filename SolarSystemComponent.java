import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;
import java.awt.Color;

/**
 * Class that creates instances of the classes that comprise the cityscape and delegates drawing the
 *  cityscape to these object.
 */
public class SolarSystemComponent extends JComponent
{
    // define the objects in your Cityscape as instance variables
    // ...
    private CityBuilding tower;
    private CityBuilding tower2;
    private Moon moon;
    private CityBuilding grass;
    private Ghost ghost1;
    private CityBuilding tower3;
    private CityBuilding tower4;
    private CityBuilding tower5;
    private CityBuilding tower6;
    private CityBuilding tower7;
    private CityBuilding tower8;
    private CityBuilding tower9;
    private Ghost ghost2;
    

    // define the Component contructor and intiailize all instance variables
    // ...
    /**
     * Defines objects and constructs them
     */
    public CityscapeComponent()
    {
        Color gras = new Color(47, 78, 60);
        Color twr1 = new Color(122,127,152);
        Color twr2 = new Color(117,117,188);
        Color twr3 = new Color(43,57,97);
        Color twr4 = new Color(79,127,148);
        Color twr5 = new Color(125,119,156);
        Color twr6 = new Color(112,131,165);
        Color twr7 = new Color(71,77,88);
        Color twr8 = new Color(102,102,153);
        Color twr9 = new Color(67,67,124);
        
        this.tower = new CityBuilding(80, 40, twr1, 100, 350);
        this.tower2 = new CityBuilding(110, 50, twr2, 170, 320);
        this.moon = new Moon(50, Color.white, 50, 50);
        this.grass = new CityBuilding(100,700,gras,0, 430);
        this.ghost1 = new Ghost(Color.white, Color.black, 30, 10, 150);
        this.tower3 = new CityBuilding(95,50,twr3, 20, 335);
        this.tower4 = new CityBuilding(125, 40,twr4,240,305);
        this.tower5 = new CityBuilding(100,50,twr5,300,330);
        this.tower6 = new CityBuilding(160,50,twr6,370,270);
        this.tower7 = new CityBuilding(160,50,twr7,440,270);
        this.tower8 = new CityBuilding(140,50,twr8,510,290);
        this.tower9 = new CityBuilding(120,60,twr9,590,310);
        this.ghost2 = new Ghost(Color.black, Color.gray, 30,701,150);
        
    }

    /**
     * This method is invoked by the Java Run-Time whenever the component needs to be redrawn.
     * It does not need to be invoked explicitly.
     * 
     * @param g a reference to the Graphics object used for all drawing operations
     *
     */
    @Override
    public void paintComponent(Graphics g)
    {
        Graphics2D g2 = (Graphics2D) g;

        // invoke the draw method on each object in your Cityscape
        // ...

        this.tower.draw(g2);
        this.tower2.draw(g2);
        this.moon.draw(g2);
        this.grass.draw(g2);
        this.ghost1.draw(g2);
        this.tower3.draw(g2);
        this.tower4.draw(g2);
        this.tower5.draw(g2);
        this.tower6.draw(g2);
        this.tower7.draw(g2);
        this.tower8.draw(g2);
        this.tower9.draw(g2);
        this.ghost2.draw(g2);

    }

    /**
     * Animate the cityscape by updating the objects such that they appear to be animated when
     *      they are next drawn.
     *
     */
    public void nextFrame()
    {
        // update the objects in the cityscape so they are animated
        // ...
        ghost1.moveRight();
        ghost2.moveLeft();

        
        // request that the Java Runtime repaints this component by invoking its paintComponent method
        //  do not explicitly invoke the paintComponent method
        repaint();
    }

}