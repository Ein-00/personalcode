
class TwoD{
	int x,y;
	TwoD(int a,int b){
		x =a;
		y = b;
	}

}
class ThreeD extends TwoD{
	int z;
	ThreeD(int a, int b, int c){
		super(a,b);
		z =c;
	}
	

}
class FourD extends ThreeD{
	int t;
	FourD(int a,int b,int c ,int t){
		super(a,b,c);
		this.t = t;
	}

}

class coords <T extends TwoD> {
	T coordsarr;
	coords(T o){
		coordsarr = o;
	}
}
class BoundedW{
	static void showxy(coords <?> c){
		System.out.println(c.coordsarr.x+' '+c.coordsarr.y);

	}
	static void showxyz(coords < ? extends ThreeD> c){
		System.out.println(c.coordsarr.x+' '+c.coordsarr.y+' '+c.coordsarr.z);
	}
	static void showall(coords < ? extends FourD> c){
		System.out.println(c.coordsarr.x+' '+c.coordsarr.y+' '+c.coordsarr.z+' '+c.coordsarr.t);
	}


	public static void main(String [] args){
		TwoD d2 = new TwoD(5,6);
		coords< TwoD> ob2 = new coords<TwoD>(d2);

		ThreeD t3 = new ThreeD(5,6,7);
		coords<ThreeD> ob3 = new coords<ThreeD>(t3);
		FourD f4 = new FourD(5,6,7,8);
		coords< FourD> ob4 = new coords<FourD>(f4);
		showxy(ob2);
		showxy(ob3);
		showxy(ob4);
		showxyz(ob3);
		showxyz(ob4);
		showall(ob4);
		
		// showall(ob2);
		// showxyz(ob2);




	}
}
