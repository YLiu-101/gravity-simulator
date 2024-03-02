import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;
import java.awt.Color;
import java.util.*;
import java.awt.geom.*;

public class Mercury extends Planet
{
    private Ellipse2D.Double mercuryOutline;
    private double x;
    private double y;
    private double w;
    private double h;

    public Mercury(double centerX, double centerY)
    {
        w = 3032.95;
        h = 3032.95;
        this.x = centerX - (w / 2);
        this.y = centerY - (h / 2);
    }

    public void movePlanet(double changeX, double changeY)
    {
        this.x += changeX;
        this.y += changeY;
    }

    public void draw(Graphics2D g2)
    {
        mercuryOutline = new Ellipse2D.Double(x, y, w, h);
    }
}
