#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// ================= stos ---------------------

#define STACK_MAX_LEN 200
int const STACK_IS_FULL = 3;
int const STACK_IS_EMPTY = 2;
int const STACK_OK = 1;
int stack_top = 0;
int stack[STACK_MAX_LEN + 1];


// ================= Item ---------------------
typedef struct ITEM
{
    int data;
    struct ITEM *next;
} Item;


// ================= Queue ---------------------
typedef struct
{
    Item *first;
    Item *last;
    int length;
} Queue;


// ================= Graph ---------------------
typedef struct
{
    int vertices_count;      // liczba wierzchołkw grafu
    bool **adjacency_matrix; // macierz sąsiedztwa
    bool is_directed;        // graph is directed
} Graph;


int push(int x);
int pop();
int get_stack_state();
int get_stack_top_value();
void eject(Queue *q);
void inject(Queue *q, int w);
void clearQueue(Queue *q);
int front(Queue const *q);
bool is_queue_empty(Queue q);
void init_queue(Queue *q);



void clear() { stack_top = 0; }


int get_stack_state()
{
    switch (stack_top)
    {
    case 0:
        return (STACK_IS_EMPTY);
    case STACK_MAX_LEN + 1:
        return (STACK_IS_FULL);
    default:
        return (STACK_OK);
    }
}

int get_stack_top_value()
{
    return stack[stack_top - 1];
}

int push(int x)
{
    if (stack_top <= STACK_MAX_LEN)
    {
        printf("\t++ Pushing vertex %c to stack. ", (char)('A' + x));
        stack[stack_top++] = x;
        printf("Stack length = %d", stack_top);
        return (STACK_OK);
    }
    else
        return (STACK_IS_FULL);
}

int pop()
{
    if (stack_top > 0)
    {
        printf("\t-- Popping vertex %c", (char)('A' + stack[stack_top - 1]));
        stack_top--;
        if (stack_top != 0)
            printf(" and going back to vertex %c", (char)('A' + stack[stack_top - 1]));
        printf(". Stack length = %d", stack_top);
        return (STACK_OK);
    }
    else
        return (STACK_IS_EMPTY);
}



void init(Graph *, int, bool);      // inicjalizacja struktury Graph
void add_edge(Graph *, int, int);   // dodanie krawędzi
void display(Graph const *);        // wyświetlenie grafu
void dfs(Graph *, int);             // wyszukiwanie "wgłąb"
void bfs(Graph *, int);             // wyszukiwanie "wszerz"
int get_unvisited_vertex(Graph *, int, bool const visited[]);
void display_vertex(int);

void init(Graph *graph, int vertices_count, bool is_directed)
{
    int vertex, start_vertex, end_vertex;
    graph->is_directed = is_directed;
    graph->vertices_count = vertices_count;
    graph->adjacency_matrix = calloc(vertices_count, sizeof(bool *)); // allocate memory for first dimension
    for (vertex = 0; vertex < vertices_count; ++vertex)
    {
        graph->adjacency_matrix[vertex] = calloc(vertices_count, sizeof(bool)); // allocate memory for second dimension
    }
    for (end_vertex = 0; end_vertex < vertices_count; ++end_vertex)
    {
        for (start_vertex = 0; start_vertex < vertices_count; ++start_vertex)
        {
            graph->adjacency_matrix[start_vertex][end_vertex] = false; // set default value for adjacency matrix
        }
    }
}

void add_edge(Graph *graph, int start_vertex, int end_vertex)
{
    if (start_vertex >= 0 && start_vertex < graph->vertices_count && end_vertex >= 0 && end_vertex < graph->vertices_count)
    {
        graph->adjacency_matrix[start_vertex][end_vertex] = true; // start pointing at end
        if (graph->is_directed == true)
            graph->adjacency_matrix[end_vertex][start_vertex] = true; // end pointing at start
    }
    else
    {
        printf("Incorrect data\n\n");
        exit(EXIT_FAILURE);
    }
}

void display_vertex(int vertex)
{
    printf("%c ", 'A' + vertex);
}

void display(Graph const *graph)
{
    int row, col;
    printf("\nGraph edges:\n");
    for (row = 0; row < graph->vertices_count; ++row)
    {
        for (col = 0; col < graph->vertices_count; ++col)
        {
            if (graph->adjacency_matrix[row][col])
            {
                printf("%c%c", (char)('A' + row), '-');
                printf("%c%c", (char)('A' + col), ' ');
            }
            if ((col + 1) == graph->vertices_count)
                printf("\n");
        }
    }
}

// zwraca nie odwiedzony wierzcho�ek przyleg�y do a
// zwraca -1, je�eli takiego wierzcho�ka nie ma
int get_unvisited_vertex(Graph *graph, int vertex, bool const visited[])
{
    int end_vertex;
    for (end_vertex = 0; end_vertex < graph->vertices_count; ++end_vertex)
    {
        if (graph->adjacency_matrix[vertex][end_vertex] && !visited[end_vertex])
        {
            return end_vertex;
        }
    }
    return -1;
}

// ================= DFS ------------------------

void dfs(Graph *graph, int start_vertex)
{
    bool *vertices_to_visit = calloc(graph->vertices_count, sizeof(bool));
    int k, visited_vertices_count = 1;
    for (k = 0; k < graph->vertices_count; ++k)
        vertices_to_visit[k] = false;
    vertices_to_visit[start_vertex] = true; // rozpocznij od wierzcho�ka a
    printf("DFS:\n");
    display_vertex(start_vertex); // wy�wietl wierzcho�ek
    push(start_vertex);           // zapisz na stos
    while (get_stack_state() == STACK_OK)
    {
        // pobierz nie odwiedzony wierzcho�ek,
        // przyleg�y do szczytowego elementu stosu
        printf("\n");
        int not_visited_vertex = get_unvisited_vertex(graph, get_stack_top_value(), vertices_to_visit);
        if (not_visited_vertex == -1)
        { // je�eli nie ma takiego wierzcho�ka,
            pop();
        }
        else
        {

            vertices_to_visit[not_visited_vertex] = true;
            display_vertex(not_visited_vertex);
            push(not_visited_vertex);
            visited_vertices_count++;
        }
    } // while
    free(vertices_to_visit);
    printf("\n");
    printf("\nGraph has %d vertices. %d was visited. Graph is%sconnected.\n\n", graph->vertices_count, visited_vertices_count, visited_vertices_count == graph->vertices_count ? " " : " not ");
}

// ================= BFS -----------------------

void bfs(Graph *graph, int start_vertex)
{
    bool *visited = calloc(graph->vertices_count, sizeof(bool));
    for (unsigned k = 0; k < graph->vertices_count; ++k)
        visited[k] = false;
    Queue q;
    init_queue(&q);
    visited[start_vertex] = true;
    display_vertex(start_vertex);
    inject(&q, start_vertex); // wstaw na końcu
    printf("\n");
    while (!is_queue_empty(q))
    {
        int b = front(&q); // pobierz pierwszy wierzchołek
        eject(&q);         // usuń go z kolejki
        printf("\n");
        int c;             // dopóki ma nie odwiedzonych sąsiadów
        while ((c = get_unvisited_vertex(graph, b, visited)) != -1)
        {
            visited[c] = true;
            display_vertex(c);
            inject(&q, c);
            printf("\n");
        }
    } // while(kolejka nie jest pusta)
    free(visited);
}

void init_queue(Queue *q)
{
    q->first = q->last = NULL;
    q->length = 0;
}

bool is_queue_empty(Queue q)
{
    return (q.first == NULL);
}

int front(Queue const *q)
{
    return q->first->data;
}

void clearQueue(Queue *q)
{
    while (q->first != NULL)
        eject(q);
}

void inject(Queue *q, int w)
{
    Item *p = malloc(sizeof(Item));
    p->data = w;
    p->next = NULL;
    if (q->first == NULL)
    {
        q->first = q->last = p;
        q->length ++;
    }
    else
    {
        q->last->next = p;
        q->last = p;
        q->length ++;
    } // dodajeelementdokolejki
    printf("\t++ Pushing vertex %c", (char)('A' + p->data));
    printf(". Queue length = %d", q->length);
}

void eject(Queue *q)
{
    // jedenelementlubkolejkapusta
    if (q->first == q->last)
    {
        Item *p = q->first;
        q->length --;
        printf("\t-- Popping vertex %c", (char)('A' + p->data));
        printf(". Queue length = %d", q->length);
        free(q->first);
        q->first = q->last = NULL;
        
    }
    else
    {
        Item *p = q->first;
        q->length --;
        printf("\t-- Popping vertex %c", (char)('A' + p->data));
        printf(". Queue length = %d", q->length);
        q->first = p->next;
        free(p);
    }
} // usuwaelementzkolejki

// ================= program -----------------------

int main()
{
    int number_of_vertices = 6;
    bool is_directed = true;
    Graph *graph;
    graph = malloc(sizeof(Graph));

    init(graph, number_of_vertices, is_directed);

    add_edge(graph, 0, 1);
    add_edge(graph, 0, 2);
    add_edge(graph, 1, 4);
    add_edge(graph, 1, 3);
    add_edge(graph, 2, 3);
    add_edge(graph, 2, 5);
    add_edge(graph, 3, 0);
    add_edge(graph, 4, 3);

    display(graph);
    bfs(graph, 3);
    return 0;
}
