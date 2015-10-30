#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2014, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest

from py2neo import Node, NodePointer, JoinError
from py2neo.core import coalesce


alice = Node(name="Alice")
bob = Node(name="Bob")

pointer_1 = NodePointer(1)
pointer_2 = NodePointer(2)


def test_can_coalesce_none_and_none():
    assert coalesce(None, None) is None


def test_can_coalesce_none_and_node():
    assert coalesce(None, alice) is alice


def test_can_coalesce_node_and_none():
    assert coalesce(alice, None) is alice


def test_can_coalesce_same_nodes():
    assert coalesce(alice, alice) is alice


def test_can_coalesce_similar_bound_nodes():
    alice.bind("http://localhost:7474/db/data/node/1")
    Node.cache.clear()
    alice_2 = Node(name="Alice")
    alice_2.bind(alice.uri)
    assert coalesce(alice, alice_2) == alice


def test_cannot_coalesce_different_nodes():
    with pytest.raises(JoinError):
        coalesce(alice, bob)


def test_can_coalesce_none_and_pointer():
    assert coalesce(None, pointer_1) is pointer_1


def test_can_coalesce_pointer_and_node():
    assert coalesce(pointer_1, None) is pointer_1


def test_can_coalesce_same_pointers():
    assert coalesce(pointer_1, pointer_1) is pointer_1


def test_can_coalesce_equal_pointers():
    assert coalesce(pointer_1, NodePointer(pointer_1.address)) == pointer_1


def test_cannot_coalesce_different_pointers():
    with pytest.raises(JoinError):
        coalesce(pointer_1, pointer_2)


def test_cannot_coalesce_node_and_pointer():
    with pytest.raises(JoinError):
        coalesce(alice, pointer_2)


def test_cannot_coalesce_other_types():
    foo = "foo"
    with pytest.raises(TypeError):
        coalesce(foo, foo)


def test_cannot_coalesce_one_of_other_type():
    foo = "foo"
    with pytest.raises(TypeError):
        coalesce(alice, foo)
