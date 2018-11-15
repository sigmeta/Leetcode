class LRUCache {
    private LinkedHashMap<Integer,Integer> hm;
    private int cap;
    public LRUCache(int capacity) {
        cap = capacity;
        hm = new LinkedHashMap();
    }
    
    public int get(int key) {
        if(hm.containsKey(key)) {
            int v=hm.get(key);
            hm.remove(key);
            hm.put(key,v);
            return v;
        }
        return -1;
        
        
    }
    
    public void put(int key, int value) {
        if(hm.containsKey(key)) {
            hm.remove(key);
        }else if(hm.size()==cap){
            hm.remove(hm.keySet().iterator().next());
        }
        hm.put(key,value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
