public class MyHashMap<K, V> {
    private MyEntry<K, V>[] table;
    private int capacity = 16; // Initial capacity
    private int size = 0; // Number of key-value pairs
    private final float loadFactor = 0.75f;
    private int threshold;

    @SuppressWarnings("unchecked")
    public MyHashMap() {
        table = new MyEntry[capacity];
        threshold = (int) (capacity * loadFactor);
    }

    private int hash(K key) {
        return Math.abs(key.hashCode()) % capacity;
    }

    /* stores the key value pair in a certain index of the table
     * if there are collisions, then adds a next pointer to each MyEntry node to make it like a LinkedList
     */
    public void put(K key, V value) {
        if (size >= threshold) {
            resize();
        }

        int hash = hash(key);
        MyEntry<K, V> newEntry = new MyEntry<>(key, value);

        if (table[hash] == null) {
            table[hash] = newEntry;
        } else {
            MyEntry<K, V> previous = null;
            MyEntry<K, V> current = table[hash];

            while (current != null) {
                if (current.key.equals(key)) {
                    if (previous == null) { // Node has to be inserted at the start of the list
                        newEntry.next = current.next;
                        table[hash] = newEntry;
                    } else {
                        newEntry.next = current.next;
                        previous.next = newEntry;
                    }
                    return;
                }
                previous = current;
                current = current.next;
            }
            previous.next = newEntry;
        }
        size++;
    }

    public V get(K key) {
        int hash = hash(key);
        if (table[hash] == null) {
            return null;
        } else {
            MyEntry<K, V> temp = table[hash];
            while (temp != null) {
                if (temp.key.equals(key)) {
                    return temp.value;
                }
                temp = temp.next;
            }
            return null; // Return null if key not found
        }
    }

    public boolean remove(K key) {
        int hash = hash(key);

        if (table[hash] == null) {
            return false;
        } else {
            MyEntry<K, V> previous = null;
            MyEntry<K, V> current = table[hash];

            while (current != null) {
                if (current.key.equals(key)) {
                    if (previous == null) { // Delete first entry node
                        table[hash] = table[hash].next;
                    } else {
                        previous.next = current.next;
                    }
                    size--;
                    return true;
                }
                previous = current;
                current = current.next;
            }
            return false;
        }
    }

    /* Resizing the HashMap if the size >= load factor * capacity */
    @SuppressWarnings("unchecked")
    private void resize() {
        capacity *= 2;
        threshold = (int) (capacity * loadFactor);
        MyEntry<K, V>[] oldTable = table;
        table = new MyEntry[capacity];
        size = 0;

        for (MyEntry<K, V> entry : oldTable) {
            if (entry != null) {
                MyEntry<K, V> current = entry;
                while (current != null) {
                    put(current.key, current.value);
                    current = current.next;
                }
            }
        }
    }

    public static void main(String[] args) {
        MyHashMap<String, Integer> map = new MyHashMap<>();
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        map.put("four", 4);
        map.put("five", 5);
        map.put("six", 6);
        map.put("seven", 7);
        map.put("eight", 8);
        map.put("nine", 9);
        map.put("ten", 10);
        map.put("eleven", 11);
        map.put("twelve", 12);

        System.out.println(map.get("one"));    // Output: 1
        System.out.println(map.get("two"));    // Output: 2
        System.out.println(map.get("three"));  // Output: 3
        System.out.println(map.get("four"));   // Output: 4
        System.out.println(map.get("five"));   // Output: 5
        System.out.println(map.get("six"));    // Output: 6
        System.out.println(map.get("seven"));  // Output: 7
        System.out.println(map.get("eight"));  // Output: 8
        System.out.println(map.get("nine"));   // Output: 9
        System.out.println(map.get("ten"));    // Output: 10
        System.out.println(map.get("eleven")); // Output: 11
        System.out.println(map.get("twelve")); // Output: 12

        map.remove("six");
        System.out.println(map.get("six"));    // Output: null
    }
}