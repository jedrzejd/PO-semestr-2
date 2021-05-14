package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        File file = new File("/tmp/" + input + ".txt");
        try {
            sc = new Scanner(file);
             ArrayList<String> n1 = new ArrayList<String>();
             ArrayList<String> n2 = new ArrayList<String>();
             ArrayList<Integer> n3 = new ArrayList<Integer>();
             ArrayList<Float> n4 = new ArrayList<Float>();
            String g1,g2;
            int g3;
            float g4=-1;
            while(sc.hasNextLine()){
                String line = sc.nextLine();
                System.out.println(line.toString());

                 String[] asd = line.split(" ");
                 String name = asd[0], surename = asd[1];
                 int year = Integer.parseInt(asd[2]);
                 float accuracy = Float.parseFloat(asd[3]);


                 if(name.length()>3 && surename.length()>=3){
                     if(surename.subSequence(surename.length()-3, surename.length()).equals("ski") && accuracy > g4){
                         g1 = name;
                         g2 = surename;
                         g3 = year;
                         g4 = accuracy;
                         n1.clear();n1.add(g1);
                         n2.clear();n2.add(g2);
                         n3.clear();n3.add(g3);
                         n4.clear();n4.add(g4);
                     }
                     else if(surename.subSequence(surename.length()-3, surename.length()).equals("ski") && accuracy == g4){
                         g1 = name;
                         g2 = surename;
                         g3 = year;
                         g4 = accuracy;
                         n1.add(g1);
                         n2.add(g2);
                         n3.add(g3);
                         n4.add(g4);
                     }
                 }

            }
             sc.close();
             File aaaa = new File("/tmp/" + input + ".max");
             PrintWriter writer = new PrintWriter(aaaa);

             for(int i=0; i<n1.size(); i++){
                 String g11,g22;
                 int g33;
                 g11 = n1.get(i);
                 String a1="", a2="";
                 a1 = a1.concat(g11.substring(0,1));
                 for(int j=0; j<g11.length()-4; j++){
                     a1 = a1.concat("*");
                 }
                 a1 = a1.concat(g11.substring(g11.length()-3,g11.length()));
                 g22 = n2.get(i);
                 a2 = a2.concat(g22.substring(0,1));
                 for(int j=0; j<g22.length()-4; j++){
                     a2 = a2.concat("*");
                 }
                 a2 = a2.concat(g22.substring(g22.length()-3,g22.length()));
                 g33 = n3.get(i);

                 writer.print(a1+" ");writer.print(a2+" ");writer.println(g33);
                 System.out.println(a1);
                 System.out.println(a2);
                 System.out.println(g33);
             }
             writer.close();
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
