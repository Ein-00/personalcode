
class Box{
	double width;
	double height;
	double depth;
	
	void print(){
		System.out.println(width+" "+depth+" "+height);
	}
	
}

class test1{
	public static void main(String[] args){
		Box b = new Box();
		b.width = 5;
		b.height = 5;
		b.depth = 5;
		System.out.println(b.width);
		b.print();
	}
}
