import java.util.ArrayList;
import java.util.HashMap;

class index{
  public static void main(String[] args) {
    HashMap<Integer,Integer> mp = new HashMap<>();
    ArrayList<Integer> li = new ArrayList<>();
    int n=18268671;
    int rem;
    while(n>0){
      rem=n%10;
      mp.put(rem,mp.getOrDefault(rem,0)+1);
      li.add(rem);
      n=n/10;
    }
    System.out.println(li);
    System.out.println(mp);
  }
}