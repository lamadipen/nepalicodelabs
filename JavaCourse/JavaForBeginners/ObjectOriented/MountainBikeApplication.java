public class MountainBikeApplication{
	public static void main(String [] args){
		MountainBike mountainBike = new MountainBike();

		mountainBike.gears = 3;

		mountainBike.ride();
		mountainBike.shiftGear();

		System.out.println("This is BMX");
		Bmx bmx = new Bmx();

		bmx.gears = 6;

		bmx.shiftGear();	

	}

}


