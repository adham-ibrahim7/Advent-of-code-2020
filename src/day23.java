/*
 * Created by Adham Ibrahim on 12/23/2020
 */

public class day23 {
    private static class Node {
        int val;
        Node next;

        Node(int val) {
            this.val = val;
        }

        public String toString(int headVal) {
            if (val == headVal) {
                return "...";
            }

            return val + " <-> " + next.toString(headVal);
        }

        public String toString() {
            return val + " <-> " + next.toString(this.val);
        }
    }

    public static void main(String[] args) {
        int[] init = {3,6,2,9,8,1,7,5,4};

        Node[] nodes = new Node[init.length+1];
        Node head = new Node(init[0]);
        Node curr = head;
        nodes[init[0]] = head;
        for (int i = 1; i < init.length; i++) {
            curr.next = new Node(init[i]);
            curr = curr.next;
            nodes[init[i]] = curr;
        }
        nodes[init[init.length-1]].next = head;

        for (int i = 0; i < 100; i++) {
            head = iterate(head, nodes);
        }

        System.out.print("p1: ");
        for (Node node = nodes[1].next; node != nodes[1]; node = node.next) {
            System.out.print(node.val);
        }
        System.out.println();

        int MAX = 1_000_000;
        nodes = new Node[MAX+1];
        head = new Node(init[0]);
        curr = head;
        nodes[init[0]] = head;
        for (int i = 1; i < MAX; i++) {
            int val = i < init.length ? init[i] : i+1;
            curr.next = new Node(val);
            curr = curr.next;
            nodes[val] = curr;
        }
        nodes[MAX].next = head;

        for (int i = 0; i < 10_000_000; i++) {
            head = iterate(head, nodes);
        }

        System.out.println("p2: " + ((long) nodes[1].next.val * nodes[1].next.next.val));
    }

    static Node iterate(Node head, Node[] nodes) {
        Node pickedUp = head.next;
        head.next = pickedUp.next.next.next;
        pickedUp.next.next.next = null;

        int destination = head.val - 1;
        if (destination == 0)
            destination = nodes.length-1;
        while (destination == pickedUp.val ||
                destination == pickedUp.next.val ||
                destination == pickedUp.next.next.val) {
            destination--;
            if (destination == 0)
                destination = nodes.length-1;
        }

        Node destinationNode = nodes[destination];
        pickedUp.next.next.next = destinationNode.next;
        destinationNode.next = pickedUp;

        return head.next;
    }
}
