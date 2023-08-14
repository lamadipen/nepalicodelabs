/**
 You will be supplied with two data files in CSV format. The first file containsstatistics about various dinosaurs. The second file contains additional data.
 Given the following formula,
  
 speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
 Where g = 9.8 m/s^2 (acceleration due to gravity on earth)
 
 Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.
  
  === Input data files ===
  
  $ cat dataset1.csv
  NAME,LEG_LENGTH,DIET
  Hadrosaurus,1.2,herbivore
  Struthiomimus,0.92,omnivore
  Velociraptor,1.0,carnivore
  Triceratops,0.87,herbivore
  Euoplocephalus,1.6,herbivore
  Stegosaurus,1.40,herbivore
  Tyrannosaurus Rex,2.5,carnivore
  
  $ cat dataset2.csv
  NAME,STRIDE_LENGTH,STANCE
  Euoplocephalus,1.87,quadrupedal
  Stegosaurus,1.90,quadrupedal
  Tyrannosaurus Rex,5.76,bipedal
  Hadrosaurus,1.4,bipedal
  Deinonychus,1.21,bipedal
  Struthiomimus,1.34,bipedal
  Velociraptor,2.72,bipedal
 

 key  bipedal -> list -> Deinonychus
**/


Class Dino {
  String name;
  float legLength;
  Strin diet;
}

Class DinStrenth {
  String name;
  float strideLength;
  String stance;
}

Class DinoResult {
  String name;
  float speed;
}


Class Solution {
  private final String g = 9.8 m / s ^ 2;

  public void printBipedalSorted(String csv1, String csv2) {
    List<Dino> ds1 = transformCsv(csv1); // O(n)
    List<DinStrength> ds2 = transformCsv(csv2); // O(m)
    Map<String, Dino> ds1Map = new HashMap();

    for (Dino dino : ds1) { // O(n)
      ds1Map.put(dino.name, dino);
    }

    List<DinStrength> filteredDs2 = ds2 // O(m)
                                        .stream()
                                        .filter(din -> din.equals("bipedal"))
                                        .collect(Collectors.toList());

    PrirityQueue<DinoResult> result =
        new PriorityQueue(Comparator.comparing((d1, d2) -> d2 - d1));

    for (DinStrength ds : filteredDs2) { // O(m)
      Dino dino = ds1map.get(ds); // O(1)

      if (null != dino) {
        float speed = calculateSpeed(dino.legLength, ds.strideLength)
                          result.add(new DinoResult(dino.name, speed));
      }
    }

    printWithOrder(result);
  }
}