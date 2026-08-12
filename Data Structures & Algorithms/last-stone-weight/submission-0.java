class Solution {

    static class Heap {
        ArrayList<Integer> arr = new ArrayList<>();

        public void add(int data) {
            arr.add(data);

            int x = arr.size() - 1;

            while (x > 0) {
                int par = (x - 1) / 2;

                if (arr.get(x) > arr.get(par)) {
                    int temp = arr.get(x);
                    arr.set(x, arr.get(par));
                    arr.set(par, temp);

                    x = par;
                } else {
                    break;
                }
            }
        }

        public int remove() {
            int data = arr.get(0);

            int temp = arr.get(0);
            arr.set(0, arr.get(arr.size() - 1));
            arr.set(arr.size() - 1, temp);

            arr.remove(arr.size() - 1);

            if (!arr.isEmpty()) {
                heapify(0);
            }

            return data;
        }

        public void heapify(int i) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;

            int max = i;

            if (left < arr.size() && arr.get(left) > arr.get(max)) {
                max = left;
            }

            if (right < arr.size() && arr.get(right) > arr.get(max)) {
                max = right;
            }

            if (max != i) {
                int temp = arr.get(i);
                arr.set(i, arr.get(max));
                arr.set(max, temp);

                heapify(max);
            }
        }

        public int size() {
            return arr.size();
        }
    }

    public int lastStoneWeight(int[] stones) {

        Heap h = new Heap();

        for (int stone : stones) {
            h.add(stone);
        }

        while (h.size() > 1) {

            int first = h.remove();
            int second = h.remove();

            if (first != second) {
                h.add(first - second);
            }
        }

        if (h.size() == 1) {
            return h.remove();
        }

        return 0;
    }
}