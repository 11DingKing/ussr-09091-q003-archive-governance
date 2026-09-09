package org.example.archive;

import java.util.List;
import java.util.Objects;

public record DomainRecord(String id, List<String> errors) {
    public DomainRecord { Objects.requireNonNull(id); errors = List.copyOf(errors); }
    public boolean valid() { return errors.isEmpty(); }
}
