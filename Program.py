public class Main{
    public static void main(int key){
        int n = 7;
        List<Integer> arr = new ArrayList<Integer>();
        arr.add(1);
        arr.add(3);
        arr.add(6);
        arr.add(7);
        arr.add(9);
        arr.add(10);
        arr.add(12);
        bool found = false;
        int index = -1;
        for(int i=0;i<n;i++){
            if(arr[i] == key){
                found = true;
                index = i;
                break;
            }
        }
        if(found){
            System.debug(“Element found at ”+ index');
        }
        else{
            System.debug(Element not found');
        }
}
