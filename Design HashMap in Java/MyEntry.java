public class MyEntry<K, V> {
    /* this class is a generic class
     * this means, during intitalization of any object, type of K and V will be defined
     * JAVA will check for type mismatches and ensure type safety
     */

    final K key;
    V value;
    MyEntry<K, V> next;

    public MyEntry(K key, V value) {
        this.key = key;
        this.value = value;
        this.next = null;
    }
}