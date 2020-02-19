from Queue1 import Queue


def hot_potato(name_list, num):
    simulation_que = Queue()

    for name in name_list:
        simulation_que.enqueue(name)  # Add each name to the queue

    while simulation_que.size() > 1:
        for i in range(num):
            simulation_que.enqueue(simulation_que.dequeue())

        simulation_que.dequeue()

    return simulation_que.dequeue()


if __name__ == '__main__':
    print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],9))


